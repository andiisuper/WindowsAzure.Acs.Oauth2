# AXIOM Runtime Notes

## Storage layout

The runtime writes its state under `~/.axiom/`:

- `~/.axiom/.axiomignore`
  Default ignore rules, created automatically if missing.
- `~/.axiom/index/henry_memory.sqlite3`
  SQLite FTS text index used for lexical search, timeline, and audit.
- `~/.axiom/vectors/henry_memory.jsonl`
  Lightweight vector store with one JSON record per indexed chunk.
- `~/.axiom/cache/embedding_cache.json`
  Embedding cache keyed by chunk hash.
- `~/.axiom/last_build_report.json`
  Latest build summary and machine/profile metadata.

## Embedding backend

- Preferred: local Ollama at `http://localhost:11434/api/embeddings`
- Model default: `nomic-embed-text`
- Fallback: deterministic hash embeddings so the index still builds without Ollama

## Optional parser dependencies

The scripts run with the Python standard library alone, but these packages improve parsing coverage:

- `pypdf` for PDF extraction
- `python-docx` for DOCX files
- `openpyxl` for XLSX files
- `Pillow` and `pytesseract` for OCR

## Commands

Scoped build:

```powershell
python scripts/henry_main.py --scope C:\some\folder
```

Default local build:

```powershell
python scripts/henry_main.py
```

Search:

```powershell
python scripts/henry_main.py --search "what changed in the bridge app"
```

Timeline:

```powershell
python scripts/henry_main.py --timeline
```

Machine summary:

```powershell
python scripts/henry_main.py --explain
```

Indexed-content audit:

```powershell
python scripts/henry_main.py --audit
```

Broader local-drive scan:

```powershell
python scripts/henry_main.py --all-local --ack-sensitive-scan
```
