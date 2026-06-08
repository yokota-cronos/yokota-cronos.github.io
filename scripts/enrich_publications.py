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


def fetch_bibtex(doi):
    """Official BibTeX for the DOI via doi.org content negotiation
    (works for both Crossref and DataCite/arXiv DOIs)."""
    url = "https://doi.org/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={
        "User-Agent": "cronos-web/1.0 (mailto:%s)" % MAILTO,
        "Accept": "application/x-bibtex",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace").strip()
    except Exception as e:  # noqa: BLE001
        print("  bibtex fetch failed for %s: %s" % (doi, e), file=sys.stderr)
        return ""


ARXIV_RE = re.compile(r'(\d{4}\.\d{4,5})')


def extract_arxiv(s):
    if not s:
        return None
    m = ARXIV_RE.search(s)
    return m.group(1) if m else None


def fetch_arxiv(arxiv_id):
    """Metadata (title/authors/year) for an arXiv paper via the arXiv API."""
    import xml.etree.ElementTree as ET
    url = "http://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id)
    req = urllib.request.Request(
        url, headers={"User-Agent": "cronos-web/1.0 (mailto:%s)" % MAILTO})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read().decode("utf-8", "replace")
        ns = {"a": "http://www.w3.org/2005/Atom"}
        entry = ET.fromstring(data).find("a:entry", ns)
        if entry is None:
            return None
        te = entry.find("a:title", ns)
        title = " ".join(te.text.split()) if te is not None and te.text else ""
        authors = [ae.find("a:name", ns).text for ae in entry.findall("a:author", ns)
                   if ae.find("a:name", ns) is not None]
        pe = entry.find("a:published", ns)
        year = pe.text[:4] if pe is not None and pe.text else ""
        return {"title": title, "authors": ", ".join(authors), "year": year}
    except Exception as e:  # noqa: BLE001
        print("  arxiv fetch failed for %s: %s" % (arxiv_id, e), file=sys.stderr)
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

    # Normalize the (symbol-laden) marker column headers to stable names.
    rename = {}
    for h in fields:
        n = "".join(ch for ch in h.lower() if ch.isalnum())
        if n.startswith("first"):
            rename[h] = "first_authors"
        elif n.startswith("cores") or n.startswith("corresp"):
            rename[h] = "corresponding_authors"
    if rename:
        fields = [rename.get(h, h) for h in fields]
        for row in rows:
            for old, new in rename.items():
                if old in row:
                    row[new] = row.pop(old)
        changed = True

    # Bibliographic-detail columns are derived from Crossref (no sheet column).
    for col in ("volume", "number", "pages", "bibtex"):
        if col not in fields:
            fields.append(col)
            changed = True
        for row in rows:
            row.setdefault(col, "")

    for row in rows:
        real_doi = extract_doi(row.get("doi", ""))
        arxiv_id = extract_arxiv(row.get("arxiv", ""))
        if not real_doi and not arxiv_id:
            continue

        if real_doi:
            # Metadata from Crossref.
            msg = fetch(real_doi)
            time.sleep(1)  # be polite to the API
            if msg:
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
                # number = issue, falling back to the article number.
                detail = {
                    "volume": msg.get("volume"),
                    "number": msg.get("issue") or msg.get("article-number"),
                    "pages": msg.get("page"),
                }
                for col, v in detail.items():
                    val = str(v).strip() if v else ""
                    if (row.get(col) or "") != val:
                        row[col] = val
                        changed = True
            bibtex_doi = real_doi
        else:
            # arXiv-only: metadata from the arXiv API, BibTeX via its DataCite DOI.
            ax = fetch_arxiv(arxiv_id)
            time.sleep(1)
            if ax:
                if is_empty(row, "title") and ax.get("title"):
                    row["title"] = ax["title"]
                    changed = True
                if is_empty(row, "authors") and ax.get("authors"):
                    row["authors"] = ax["authors"]
                    changed = True
                if is_empty(row, "year") and ax.get("year"):
                    row["year"] = ax["year"]
                    changed = True
            if is_empty(row, "publisher"):
                row["publisher"] = "arXiv preprint arXiv:" + arxiv_id
                changed = True
            bibtex_doi = "10.48550/arXiv." + arxiv_id

        # Official BibTeX straight from the DOI (Crossref/DataCite), never self-made.
        bib = fetch_bibtex(bibtex_doi)
        time.sleep(1)
        if bib:
            bib = re.sub(r',\s+(\w+=)', r',\n  \1', bib)
            bib = re.sub(r'\s*\}\s*$', '\n}', bib).strip()
            if (row.get("bibtex") or "") != bib:
                row["bibtex"] = bib
                changed = True
        print("  enriched %s -> %s" % (bibtex_doi, (row.get("title") or "")[:60]))

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
