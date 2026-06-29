# AGENT_LOOP.md — Automatic Implementation + Verification

> This file defines an **automatic loop** for an AI coding agent:
> 1. Read context files on startup.
> 2. Plan implementation.
> 3. Implement.
> 4. Verify (internal + external).
> 5. Retry if needed.
> 6. Update state.
> 7. Git commit.
> 8. Move to next step.
>
> Human gives only a GOAL. Everything else is automatic.

---

## 0. Global Rules

- Read `loop-rules.md` fully before acting. Treat it as the highest-priority system spec.
- The human will provide a single **GOAL** (e.g., `GOAL: Build a CLI tool that generates markdown reports from CSV data.`).
- Once GOAL is set, **do not** ask the human for more instructions unless the loop explicitly requires input.
- All loop operations must be **autonomous**:
  - You plan steps.
  - You implement code.
  - You verify results.
  - You decide whether to retry or move forward.

---

## 1. Startup: Read Context Files

On every new session, you must read these files in order:

1. `loop-rules.md` — global constitution
2. `AGENTS.md` — project-specific config and verifier setup
3. `LOOP.md` — loop definitions and step breakdown
4. `context.md` — project description, stack, and commands
5. `state.md` — current loop state
6. `STATE.md` — global triage (if multi-loop)
7. `tasks/todo.md` — current plans
8. `tasks/lessons.md` — self-improvement patterns
9. `loop-run-log.md` — recent run history

After reading, reconstruct the current state:
- What step is in progress?
- What was the last result?
- Are there pending verifications?
- Are there lessons to apply?

---

## 2. State Management (`state.md`)

There must be a `state.md` file at the root of the repo.
If it does not exist, create it with this structure:

```markdown
# state.md — Loop State

## Goal
- <current-goal>

## Loop Status
- current_step: <string>
- implementation_attempts: <number>
- verification_attempts: <number>
- last_result: <success|fail|partial|pending>
- last_error_summary: <short text>

## Planned Steps
- [ ] step-01-...
- [ ] step-02-...

## Completed Implementations
- [x] step-01-... — <brief description>

## Log
- yyyy-mm-dd hh:mm — <action summary>

## Final Status
- goal_status: <achieved|partially_achieved|blocked>
- summary: <short narrative>
- suggestions_for_human: <what to check / review>
```

After **every** implementation and verification:
- Update `current_step`.
- Increment attempt counters.
- Set `last_result` and `last_error_summary`.
- Append a new log line describing what you did and what happened.

---

## 3. Loop Structure Overview

The loop is:

1. **PLAN_NEXT_STEP**
2. **IMPLEMENT_STEP**
3. **VERIFY_STEP** (internal + external)
4. **DECIDE_RETRY_OR_ADVANCE**
5. **UPDATE_STATE_AND_COMMIT**
6. **REPEAT UNTIL GOAL DONE OR STOP CONDITION**

---

## 4. PLAN_NEXT_STEP

### Planning Prompt (internal)

You must internally run a reasoning step like this:

> PLAN_NEXT_STEP:
> - Read `state.md` and the GOAL.
> - Determine the next concrete implementation step.
> - Each step must be small and testable.
> - Check which skills or knowledge areas are required for this step.
> - Output a short **Step Plan**:
>   - step_id: e.g. `step-01-setup`
>   - description
>   - target files to edit
>   - success criteria (explicit and verifiable)
>   - verification method (commands + external verifier)
>
> Do not edit files in this phase; just plan.

After planning, write a brief summary to `state.md` under **Loop Status** and **Log**.

---

## 5. IMPLEMENT_STEP

### Implementation Prompt (internal)

Once you have a step plan:

> IMPLEMENT_STEP:
> - Edit the repo files to perform the implementation for this step.
> - Follow these rules:
>   - Keep files formatted and idiomatic.
>   - Preserve working code; do not break unrelated parts.
>   - Follow the project's coding conventions (see `context.md`).
> - Once you finish editing:
>   - Run any relevant commands documented in `context.md` (e.g., `npm test`, `npm run lint`, `npm run build`).
>   - Capture outputs and summarize success/failure.

After implementation, update `state.md`:
- `implementation_attempts` += 1
- `last_result` = `pending-verification`
- Log what files were changed.

---

## 6. VERIFY_STEP

### Internal Verification

Run the project's own commands:

```bash
# Examples — adapt to your stack:
npm run lint
npm test
npm run build
cargo check
cargo test
pytest
```

Record exit codes and output in `state.md`.

### External Verification

Use a separate model or agent that:
- **Cannot** edit the code directly.
- Only critiques and scores the changes.

Provide the external verifier with:
- Summary of the change.
- Relevant code snippets or diffs.
- Expected behavior.
- Done criteria.

The verifier should reply with a structured result:

```json
{
  "checks": [
    {"name": "...", "status": "PASS or FAIL", "detail": "..."}
  ]
}
```

### Verification Rules

- You cannot treat your own reasoning as a substitute for VERIFY.
- If the external verifier raises concerns, treat the step as incomplete.
- If the verifier is unavailable (rate limit, timeout):
  - Mark step as `[!] verification_pending` — NOT `[x] completed`.
  - Resume verification when available.
  - Never declare done without a passing verifier verdict.

---

## 7. DECIDE_RETRY_OR_ADVANCE

### Retry Logic

> DECIDE_RETRY_OR_ADVANCE:
> - If all checks pass:
>   - Mark the step as completed under **Completed Implementations** in `state.md`.
>   - Move on to PLAN_NEXT_STEP.
> - If any check fails:
>   - Check the number of implementation attempts for this step.
>   - If attempts < MAX_STEP_ATTEMPTS (default: 3):
>     - Create a **Retry Plan** guided by verification feedback.
>     - Go back to IMPLEMENT_STEP, focused on fixes.
>   - If attempts >= MAX_STEP_ATTEMPTS:
>     - Log that the step is stuck.
>     - Mark it in `state.md` as `[!] Step N: stuck after MAX attempts`.
>     - Move on to the next step to avoid infinite loops.

Always append a log entry describing the decision.

---

## 8. UPDATE_STATE_AND_COMMIT

After each **completed step** (whether success or stuck):

1. Ensure `state.md` is updated.
2. Stage changes:
   ```bash
   git add .
   ```
3. Commit with a descriptive message:
   ```bash
   git commit -m "loop: <step_id> <status>"
   ```
   Examples:
   - `git commit -m "loop: step-01-setup success"`
   - `git commit -m "loop: step-02-gsap-scroll stuck (3 attempts)"`
4. Do **not** push automatically unless explicitly instructed.

---

## 9. STOP CONDITION

The loop stops automatically when:

- All planned steps under **Completed Implementations** in `state.md` are either `[x] completed` or `[!] stuck`, **and**
- The agent determines that the GOAL is either:
  - Achieved (core functionality works and passes tests), or
  - Cannot be further improved without human intervention.

On stop:

1. Add a final section in `state.md`:

```markdown
## Final Status
- goal_status: <achieved|partially_achieved|blocked>
- summary: <short narrative summary>
- suggestions_for_human: <what to check / review / change>
```

2. Make one last git commit:
   ```bash
   git commit -m "loop: final status <goal_status>"
   ```

---

## 10. Agent Behavior Summary

- Read `loop-rules.md` as your **constitution**.
- Read this file as your **execution algorithm**.
- Ask the human only for:
  - GOAL (once at the start).
- Then:
  - Plan → implement → verify → retry/advance.
  - Update `state.md` every time.
  - Commit every completed step.
  - Stop when the GOAL is reasonably achieved or blocked.

Do not deviate from this loop unless the human changes the GOAL or explicitly instructs you to modify the loop configuration.
