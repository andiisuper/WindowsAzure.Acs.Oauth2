# Henry AXIOM Self Build

Local-first Codex skill for building and querying a scoped machine knowledge index.

## Contents

- `SKILL.md`
  Skill instructions and safety gates.
- `agents/openai.yaml`
  Codex UI metadata.
- `scripts/`
  Discovery, parsing, indexing, and retrieval runtime.
- `references/`
  Compliance and runtime notes.

## Run

Print the machine profile:

```powershell
python "scripts/henry_main.py" --profile
```

Build a scoped index:

```powershell
python "scripts/henry_main.py" --scope "C:\openAICodex\jotform-smart-bridge"
```

Search the saved index:

```powershell
python "scripts/henry_main.py" --search "Jotform bridge OCR"
```

## Safety

- Scoped local indexing is the default.
- Broader scans require `--ack-sensitive-scan`.
- Secrets and common regulated folders are excluded by default through `~/.axiom/.axiomignore`.
