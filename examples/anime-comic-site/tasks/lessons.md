# tasks/lessons.md — Self-Improvement & Mistake Patterns

This file is the **learning store** for agents.
Every time a user corrects the agent or a loop iteration fails, record a lesson here.

Agents must read relevant lessons at the start of a session.

---

## 1. Usage Rules

- After ANY correction by the user:
  - Add a new lesson entry with context, mistake, and new rules.
- Lessons should be short, actionable, and domain-mapped.
- Before planning/implementing: scan for relevant lessons.

---

## 2. Lessons

### L-001 — React Structure & File Organization

- **Context**: Component placement and file naming in a React app.
- **Mistake**: Mixed 3D scene code and section layout code in a single oversized component.
- **Rules**: Always separate `3DScene` from `sections`. Use dedicated directories.

### L-002 — Scroll & Animation Safety

- **Context**: GSAP ScrollTrigger integration with 3D camera.
- **Mistake**: Overly aggressive camera jumps causing disorientation.
- **Rules**: Prefer smooth easing, incremental camera changes. Test on multiple viewports.

### L-003 — Loop & State Consistency

- **Context**: Updating loop state across files.
- **Mistake**: Updated code but forgot to update `state.md` and `tasks/todo.md`.
- **Rules**: After each implementation + verification cycle, update all state files and commit.

### L-004 — Deterministic Verification > Model Assertions

- **Context**: Running build/TS verification via AI agent.
- **Mistake**: Delegated build pass/fail verdict to model's assertion instead of checking exit codes.
- **Rules**: Run commands directly. Exit code 0 + no errors = truth. Model is a reviewer, not the owner of build verdicts.

### L-005 — External Verifier Required Before "Done"

- **Context**: Design overhaul: internal checks passed but external verifier was rate-limited.
- **Mistake**: Marked steps as completed without passing external verifier verdict.
- **Rules**: Canonical loop order is IMPLEMENT → VERIFY (external) → DONE. If verifier unavailable, mark `[!] verification_pending` — not `[x] completed`.

---

## 3. Pending Lessons

- 2026-06-28 13:45 — [agent] Verification must use real CLI exit codes, not model assertions.
- 2026-06-28 14:40 — [agent] External verifier is mandatory before marking done.

---

## 4. How Agents Use This File

- On session start: read `tasks/lessons.md`.
- Apply domain-specific rules when planning and implementing.
- New lessons become rules for future sessions.
