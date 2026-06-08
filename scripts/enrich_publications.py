#!/usr/bin/env python3
"""Fill in missing publication fields from the DOI via the Crossref API.

The publications spreadsheet may contain a row with only a DOI (and maybe a
publisher). This script looks up that DOI and fills EMPTY fields only
(title, authors, year, publisher) — it never overwrites values already set
in the sheet. Run after downloading the CSV in the update-data workflow,
and idempotent (re-running fills the same values, so no churn).

Usage: python3 scripts/enrich_publications.py [path/to/publications.csv]
"""
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else "_data/publications.csv"
MAILTO = "takahashi@akg.t.u-tokyo.ac.jp"
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s"<>]+')


def extract_doi(s):
    if not s:
        return None
    m = DOI_RE.search(s)
    if not m:
        return None
    return m.group(0).rstrip('.,;)')


def fetch(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(
        url, headers={"User-Agent": "cronos-web/1.0 (mailto:%s)" % MAILTO}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("message")
    except Exception as e:  # noqa: BLE001
        print("  crossref fetch failed for %s: %s" % (doi, e), file=sys.stderr)
        return None


def first(x):
    if isinstance(x, list):
        return x[0] if x else ""
    return x or ""


def authors_str(msg):
    out = []
    for a in (msg.get("author") or []):
        name = (a.get("given", "") + " " + a.get("family", "")).strip()
        if not name:
            name = a.get("name", "")
        if name:
            out.append(name)
    return ", ".join(out)


def year_str(msg):
    for key in ("issued", "published", "published-online", "published-print"):
        dp = (msg.get(key) or {}).get("date-parts") or []
        if dp and dp[0] and dp[0][0]:
            return str(dp[0][0])
    return ""


def is_empty(row, key):
    return not (row.get(key) or "").strip()


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    if not fields:
        print("empty CSV; nothing to do")
        return
    fields = list(fields)

    changed = False

    # Bibliographic-detail columns are derived from Crossref (no sheet column).
    for col in ("volume", "number", "pages"):
        if col not in fields:
            fields.append(col)
            changed = True
        for row in rows:
            row.setdefault(col, "")

    for row in rows:
        doi = extract_doi(row.get("doi", ""))
        if not doi:
            continue
        msg = fetch(doi)
        time.sleep(1)  # be polite to the Crossref API
        if not msg:
            continue
        # Fill empty core fields only — never overwrite values set in the sheet.
        if is_empty(row, "title"):
            t = first(msg.get("title"))
            if t:
                row["title"] = t
                changed = True
        if is_empty(row, "authors"):
            a = authors_str(msg)
            if a:
                row["authors"] = a
                changed = True
        if is_empty(row, "year"):
            y = year_str(msg)
            if y:
                row["year"] = y
                changed = True
        if is_empty(row, "publisher"):
            c = first(msg.get("container-title")) or msg.get("publisher", "")
            if c:
                row["publisher"] = c
                changed = True
        # volume / number(issue) / pages always come from Crossref.
        for col, key in (("volume", "volume"), ("number", "issue"), ("pages", "page")):
            v = msg.get(key)
            val = str(v).strip() if v else ""
            if (row.get(col) or "") != val:
                row[col] = val
                changed = True
        print("  enriched %s -> %s" % (doi, (row.get("title") or "")[:60]))

    if changed:
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(rows)
        print("publications.csv updated")
    else:
        print("no enrichment needed")


if __name__ == "__main__":
    main()
