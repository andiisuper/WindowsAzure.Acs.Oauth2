---
name: henry-axiom-self-build
description: Use when the user wants to build, refresh, or query a reusable knowledge index over local files on this machine. This skill scaffolds and runs a safety-gated AXIOM workflow: discover scoped roots, ignore secrets and regulated folders, parse common documents and code, capture git activity, and store searchable memory for recall and timeline queries. Use for requests like "index this folder", "build machine memory", "search my files", or "what projects are here". Do not use for broad full-drive, cloud, or email ingestion unless the user explicitly asks for those sources and accepts the privacy impact.
---

# Henry AXIOM Self Build

## Overview

This skill creates and operates a local AXIOM memory builder for Henry. It is designed for repeatable file indexing and recall, but it defaults to scoped local paths and treats full-machine, cloud, and email sources as sensitive expansions that require explicit approval.

## Safety Gate

Before running any build:

- Default to user-provided `--scope` paths or the safe local defaults from the runtime.
- Do not expand to `--all-local`, `--include-cloud`, or `--include-email` unless the user explicitly wants that and the command includes `--ack-sensitive-scan`.
- Respect `~/.axiom/.axiomignore`. The runtime creates it automatically if missing.
- Secrets and regulated paths are excluded from indexing by default, including `.env`, key material, student-record folders, and common financial-document patterns.
- Read [references/compliance.md](references/compliance.md) when the request touches student, financial, credential, or other regulated data.

## Workflow

1. Confirm scope.
   For vague requests like "index everything", start with a scoped build or a machine profile first, then expand only if the user still wants a broader crawl.
2. Build or refresh the index.
   Run `python scripts/henry_main.py --scope <path>` for a targeted build, or omit `--scope` to use the runtime's safe default roots.
3. Query the memory.
   Use `--search`, `--timeline`, `--explain`, or `--audit` after a build to retrieve information from the saved index.
4. Escalate carefully.
   Only add `--all-local`, `--include-cloud`, or `--include-email` with `--ack-sensitive-scan` after the user has clearly accepted the wider privacy blast radius.

## Quick Start

Build a scoped index:

```powershell
python scripts/henry_main.py --scope C:\openAICodex\jotform-smart-bridge
```

Build using the runtime's default local roots:

```powershell
python scripts/henry_main.py
```

See the machine profile before scanning:

```powershell
python scripts/henry_main.py --profile
```

Search the saved memory:

```powershell
python scripts/henry_main.py --search "student attendance dashboard"
```

See a recent activity timeline:

```powershell
python scripts/henry_main.py --timeline
```

Run a broader scan only after explicit approval:

```powershell
python scripts/henry_main.py --all-local --ack-sensitive-scan
```

## Resources

- `scripts/henry_main.py`
  Main CLI for build, search, timeline, explain, and audit flows.
- `scripts/henry_discovery.py`
  Scoped filesystem discovery with ignore-pattern filtering and project detection.
- `scripts/henry_parser.py`
  Multi-format parser for text, code, CSV, email, PDF, DOCX, XLSX, and OCR-enabled images when optional packages exist.
- `scripts/henry_indexer.py`
  Chunking, embedding, SQLite FTS indexing, and lightweight vector-store persistence.
- `scripts/henry_retrieval.py`
  Recall, timeline, machine-summary, and indexed-content audit helpers.
- `references/compliance.md`
  Read this when the request involves sensitive data classes or broad indexing.
- `references/runtime.md`
  Read this for storage locations, optional dependencies, and backend behavior.

## Notes

- This implementation does not auto-connect live Gmail, IMAP, or Google Drive APIs. It supports local files immediately and local synced folders when the user opts in.
- If Ollama is running locally, the indexer uses it for embeddings. If not, it falls back to deterministic hash embeddings so the workflow still runs.
- The saved AXIOM state lives under `~/.axiom/`.
