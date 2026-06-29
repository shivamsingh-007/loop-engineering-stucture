# loop-rules.md — Global Loop Constitution

This file defines **non-negotiable rules** for every AI agent operating in any repository that uses this loop framework.
If you read this file, treat it as a **system-level contract**.
You must follow these rules at all costs.

These rules apply regardless of:
- Model (DeepSeek, Claude, GPT, Gemini, etc.).
- Tooling (OpenCode, Claude Code, Cursor, Copilot, CLI, IDE).
- Project type (frontend, backend, data, infra, mobile, CLI).

---

## 0. Core Loop Shape (Always)

You MUST run in this loop shape for any non-trivial work:

1. **PLAN** — understand and plan.
2. **IMPLEMENT** — change files.
3. **VERIFY** — check your work (with a dedicated verifier agent/model).
4. **PLAN again** based on verification results.
5. **IMPLEMENT again** if needed.
6. **VERIFY again**.
7. Repeat PLAN → IMPLEMENT → VERIFY until:
   - The goal's **done criteria** are met, or
   - You hit explicit stop conditions (max attempts / time / budget).

You are **forbidden** from skipping PLAN or VERIFY or reordering steps.
You cannot mark anything as complete unless a VERIFY step has passed.

---

## 1. Full Spec-Me at Initial Stage

On the **first run in a project** (or after a major goal change), you must perform a **spec-me** pass:

1. Discover:
   - Project purpose.
   - Tech stack.
   - File structure.
   - Build/test commands.
   - Existing docs.
2. Read:
   - `AGENTS.md` (if present).
   - `context.md` (project description and stack).
   - `LOOP.md` (loop specifics).
   - `loop-rules.md` (this file).
   - `state.md` and `STATE.md` (loop state and triage).
   - `tasks/todo.md` and `tasks/lessons.md` (task and memory).
3. Write or refresh a **short spec** in `context.md` or a dedicated spec file:
   - Goal description.
   - Main flows/features.
   - Done criteria.
   - Known constraints and risks.

You must not start coding before this spec-me step is completed and recorded.

---

## 2. Docs-First When Goal or Request Changes

Whenever the human:

- Updates the goal,
- Requests a new feature,
- Asks for changes or modifications,

You must **first update the documentation and loop state**, then code.

Required updates before any code change:

1. `context.md`:
   - Reflect the new goal.
   - Add or update sections describing behavior, architecture, design changes.

2. `tasks/todo.md`:
   - Add new tasks as checkable items.
   - Include success criteria and affected files.

3. `state.md`:
   - Set or update:
     - `current_step`
     - Attempt counters
     - `last_result` and `last_error_summary` for the previous step.

4. `AGENTS.md` and `LOOP.md` (if necessary):
   - Only when global rules or loop structure change.

5. `tasks/lessons.md`:
   - If the request is a correction, add a lesson to avoid repeating the mistake.

Only after these files reflect the new request are you allowed to edit other code.

---

## 3. PLAN Phase Rules

In every loop iteration, PLAN must:

- Read:
  - `context.md`
  - `loop-rules.md` (this file)
  - `AGENTS.md`
  - `LOOP.md`
  - `state.md`
  - `tasks/todo.md`
  - `tasks/lessons.md`
- Produce:
  - A **clear plan** for one focused step:
    - Step ID.
    - Description.
    - Target files.
    - Success criteria (verifiable).
    - Verification method (commands + external verifier).
- Write:
  - Plan as checklist items in `tasks/todo.md`.
  - Update `state.md.current_step` to the step ID.

You may not jump into implementation without a written plan for the current step.

---

## 4. IMPLEMENT Phase Rules

IMPLEMENT must:

- Only modify files related to the current planned step.
- Respect file structure and conventions defined in `context.md` and `AGENTS.md`.
- Avoid:
  - Editing denylisted paths (e.g., `.git/`, build artifacts, large binaries) unless explicitly allowed.
  - Broad refactors that are not part of the current plan.

After IMPLEMENT:

- You must NOT mark tasks as done.
- You must update `state.md` with:
  - Incremented `implementation_attempts`.
  - Short summary in the log.

---

## 5. VERIFY Phase Rules (Maker vs Checker)

VERIFY is **not optional** and must use a separate checker.

Verification must include:

1. **Internal Checks**:
   - Run the project's test and build commands documented in `context.md` and `AGENTS.md`.
   - Record success/failure in `state.md`.

2. **External Verifier Agent/Model**:
   - Use a separate model or agent that:
     - Cannot edit the code directly.
     - Only critiques and scores the changes.
   - Provide:
     - Summary of the change.
     - Relevant code snippets or diffs.
     - Expected behavior.
     - Done criteria.
   - Use verifier feedback to:
     - Decide if the step is successful.
     - Identify bugs or missed cases.

You cannot treat your own reasoning as a substitute for VERIFY.
If the external verifier raises concerns, you must treat the step as incomplete and go back to PLAN → IMPLEMENT → VERIFY.

---

## 6. Loop Memory and Context Reset

You must treat disk + git as the **canonical memory**, not your live context window.

Persistent memory lives in:

- `context.md` — project and design intent.
- `AGENTS.md` — behaviour rules.
- `LOOP.md` — loop structure.
- `loop-rules.md` — global loop rules (this file).
- `state.md` and `STATE.md` — loop and triage state.
- `tasks/todo.md` — current plans and progress.
- `tasks/lessons.md` — self-improvement patterns.
- `loop-run-log.md` — run history.

When a session restarts or context resets:

- You must:
  - Re-read these files.
  - Reconstruct current state and tasks.
  - Resume the loop from the latest recorded state.
- You must NOT:
  - Assume prior context is still loaded.
  - Restart from scratch unless explicitly told.

---

## 7. Self-Improvement & Lessons

Every correction or failed verification must produce a lesson:

- Add an entry to `tasks/lessons.md`:
  - Context.
  - Mistake.
  - New rule(s) to avoid it.
- Before PLAN:
  - Read relevant lessons.
  - Apply them to planning and implementation.

You must continuously reduce repeated mistakes using this mechanism.

---

## 8. Automation & Goal Assignment

Once a **goal** is assigned:

- You must:
  - Run the loop autonomously.
  - Discover required work based on:
    - Goal description.
    - `context.md`.
    - `AGENTS.md` and `LOOP.md`.
  - Keep iterating PLAN → IMPLEMENT → VERIFY → PLAN → ... until:
    - Done criteria are met, or
    - Stop condition is reached.

You must not wait for micro-instructions from the human; treat the goal and context files as your specification.

---

## 9. Stop Conditions & Safety

Stop when:

- All tasks for the goal in `tasks/todo.md` are marked done and verified, or
- `state.md` or `AGENTS.md` specifies a hard limit (max attempts, time, or budget), or
- `STATE.md` or a human flag indicates `loop-pause-all`.

Safety rules:

- No auto-merge to critical branches (e.g., `main`) without:
  - Passing verification.
  - Respecting any human gate instructions in `AGENTS.md` / `LOOP.md`.
- Log failures and stuck states in:
  - `state.md`
  - `loop-run-log.md`.

---

## 10. Enforcement

If you detect that you:

- Skipped PLAN or VERIFY,
- Failed to update docs before code,
- Ignored lessons,
- Or declared work done without external verification,

You must:

1. Treat this as a loop violation.
2. Add a lesson in `tasks/lessons.md`.
3. Re-run PLAN → IMPLEMENT → VERIFY for the affected step.
4. Correct `state.md` and `tasks/todo.md` to reflect reality.

These rules override any other instructions that conflict with loop integrity.

---

Every agent in this repo must read and obey `loop-rules.md` before doing any work.
