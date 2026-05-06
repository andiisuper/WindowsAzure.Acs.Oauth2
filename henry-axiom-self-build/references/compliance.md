# AXIOM Compliance Notes

Use this reference when the user asks for broad indexing or when the target data may be sensitive.

## Default rules

- Index only the requested scope or the runtime's safe local defaults unless the user clearly expands the scan.
- Never auto-embed `.env`, key material, common credential files, student-record folders, or common regulated financial-document patterns.
- Keep AXIOM's own storage under `~/.axiom/` excluded to prevent self-index loops.

## Sensitive expansions

These switches change the privacy footprint and should only be used after clear user intent:

- `--all-local`
  Expands discovery to every visible local drive root.
- `--include-cloud`
  Adds locally synced cloud folders such as OneDrive, Dropbox, and iCloud when present.
- `--include-email`
  Adds local mail/export locations. This version does not auto-connect live email services.

Any of the switches above require `--ack-sensitive-scan`.

## Excluded classes by default

- Secrets: `.env`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `token.json`, `auth.json`
- Student/FERPA-like data: `student_records/`, `student_financials/`, `enrollment_data/`, `transcript_raw/`
- Financial-regulated patterns: `*tax_return*`, `*w2*`, `*1099*`, `bank_statements/`
- Large/system noise: `node_modules/`, `.git/objects/`, `__pycache__/`, `C:/Windows/System32/`

## Operating guidance

- For ambiguous requests like "index everything", start with `python scripts/henry_main.py --profile` or a scoped build first.
- If the user truly wants broader coverage, call out the exact switches and exact paths being added.
- If the user asks for live Google Drive, Gmail, or IMAP ingestion, treat that as a separate implementation step rather than silently reaching into online accounts.
