# tasks/todo.md — Architecture Plan

## Current Goal

Implement a reusable loop engineering framework that can be ported to any repo.

---

## Active Tasks

### Step 1 — Global Core Files

- [x] Create `loop-rules.md` — Global loop constitution
- [x] Create `AGENT_LOOP.md` — Detailed execution algorithm
- [x] Create `multiloop.md` — Multi-loop coordination rules

### Step 2 — Global Observability Files

- [x] Create `STATE.md` — Global triage structure (same everywhere)
- [x] Create `loop-run-log.md` — Append-only run history (same format everywhere)

### Step 3 — Project Templates

- [x] Create `templates/AGENTS.md.template`
- [x] Create `templates/LOOP.md.template`
- [x] Create `templates/context.md.template`
- [x] Create `templates/state.md.template`
- [x] Create `templates/loop-run-log.md.template`
- [x] Create `templates/tasks/todo.md.template`
- [x] Create `templates/tasks/lessons.md.template`

### Step 4 — Documentation

- [x] Create `README.md` — Framework overview, porting guide, quickstart

### Step 5 — Examples (Optional)

- [x] Create `examples/anime-comic-site/` with concrete filled files

### Step 6 — Verification

- [x] Verify all files exist and are coherent
- [x] External verifier review — ALL PASS
- [x] Update state and commit

---

## Success Criteria

- All global files are project-agnostic ✓
- Templates use placeholders with clear comments ✓
- README explains how to port to any repo ✓
- External verifier confirms reusability ✓
