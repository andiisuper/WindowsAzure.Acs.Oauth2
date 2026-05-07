# Henry AXIOM Self Build

Local-first Codex skill for building and querying a scoped machine knowledge index.

## Founder Mission

Henry AXIOM is part of Di Tran's broader human-centered AI mission: build an army of practical AI agents that automates friction in daily life while elevating human dignity, quality of life, wellness, fitness, health, learning, and meaningful work.

The vision is not AI replacing humanity. The vision is AI serving humanity: organizing knowledge, reducing repetitive labor, protecting sensitive information, helping people make better decisions, and giving families, students, workers, founders, and communities more time for the human things that matter.

Henry, Codex, and the broader agent network are designed as collaborators. They help people understand their own systems, remember what matters, automate what is safe to automate, and humanize technology so it becomes more useful, trustworthy, and life-giving.

See `references/founder_mission.md` for the fuller mission statement.

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
