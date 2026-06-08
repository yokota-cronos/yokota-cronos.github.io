#!/usr/bin/env python3
"""Apply native italic/bold formatting from the Google Sheet to publication titles.

CSV export loses per-character formatting, so this reads the title column's
``textFormatRuns`` via the Google Sheets API v4 and rewrites the title in
publications.csv with <i>/<b> HTML where the sheet uses italic/bold.

Only rows whose CSV (plain) title still matches the sheet's plain title are
touched, so Crossref-filled titles are never clobbered. Titles with no
italic/bold formatting are left as plain text. No-op (exit 0) when
GOOGLE_SHEETS_API_KEY is unset, so the build still works without the key.

Usage:
  python3 scripts/enrich_titles_richtext.py <csv> <spreadsheet_id> <sheet_name>
"""
import csv
import html
import json
import os
import sys
import urllib.parse
import urllib.request

API_KEY = os.environ.get("GOOGLE_SHEETS_API_KEY", "")


def get_rowdata(sid, sheet):
    params = urllib.parse.urlencode({
        "ranges": sheet,
        "includeGridData": "true",
        "fields": "sheets(data(rowData(values("
                  "formattedValue,textFormatRuns,effectiveFormat(textFormat)))))",
        "key": API_KEY,
    })
    url = "https://sheets.googleapis.com/v4/spreadsheets/%s?%s" % (sid, params)
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.load(r)
    sheets = data.get("sheets") or []
    if not sheets:
        return []
    blocks = sheets[0].get("data") or []
    if not blocks:
        return []
    return blocks[0].get("rowData") or []


def wrap(s, fmt):
    if fmt.get("italic"):
        s = "<i>%s</i>" % s
    if fmt.get("bold"):
        s = "<b>%s</b>" % s
    return s


def cell_to_html(cell):
    """Return (html, plain). html has <i>/<b> for formatted runs; '' if no
    italic/bold anywhere (so callers can leave the plain title untouched)."""
    text = cell.get("formattedValue", "") or ""
    if not text:
        return "", ""
    base = (cell.get("effectiveFormat", {}) or {}).get("textFormat", {}) or {}
    runs = cell.get("textFormatRuns") or []

    # Build (startIndex, format) segments covering the whole string.
    segs = []
    if not runs or runs[0].get("startIndex", 0) > 0:
        segs.append((0, base))
    for run in runs:
        segs.append((run.get("startIndex", 0), run.get("format", {}) or {}))

    has_emphasis = False
    out = []
    for k, (start, fmt) in enumerate(segs):
        end = segs[k + 1][0] if k + 1 < len(segs) else len(text)
        piece = text[start:end]
        if piece == "":
            continue
        if fmt.get("italic") or fmt.get("bold"):
            has_emphasis = True
        out.append(wrap(html.escape(piece), fmt))

    if not has_emphasis:
        return "", text
    return "".join(out), text


def main():
    if len(sys.argv) < 4:
        print("usage: enrich_titles_richtext.py <csv> <spreadsheet_id> <sheet_name>")
        return
    csv_path, sid, sheet = sys.argv[1], sys.argv[2], sys.argv[3]
    if not API_KEY:
        print("GOOGLE_SHEETS_API_KEY not set; skipping rich-text titles")
        return

    try:
        rowdata = get_rowdata(sid, sheet)
    except Exception as e:  # noqa: BLE001
        print("Sheets API fetch failed: %s" % e, file=sys.stderr)
        return
    if not rowdata:
        print("no row data from Sheets API")
        return

    header = [((c.get("formattedValue", "") or "").strip())
              for c in (rowdata[0].get("values") or [])]
    tcol = next((i for i, h in enumerate(header) if h.lower() == "title"), None)
    if tcol is None:
        print("title column not found in sheet header")
        return

    html_by_plain = {}
    for r in rowdata[1:]:
        vals = r.get("values") or []
        cell = vals[tcol] if tcol < len(vals) else {}
        html_t, plain = cell_to_html(cell)
        if plain and html_t:
            html_by_plain[plain.strip()] = html_t

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)

    changed = False
    for row in rows:
        plain = (row.get("title", "") or "").strip()
        html_t = html_by_plain.get(plain)
        if html_t and html_t != row.get("title", ""):
            row["title"] = html_t
            changed = True
            print("  italicized: %s" % html_t)

    if changed:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(rows)
        print("publications.csv titles updated")
    else:
        print("no rich-text titles to apply")


if __name__ == "__main__":
    main()
