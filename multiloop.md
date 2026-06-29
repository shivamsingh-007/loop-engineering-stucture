# multiloop.md — Multi-Loop Coordination

Running more than one loop in a repo is normal.
Running them without boundaries is how loops fight each other.

This file defines **rules and wiring** for multiple long-running loops in a repository.
Each loop MUST read this file before acting.

---

## 1. Principles

1. **One owner per branch**
   - At most **one loop** may mutate a given branch **per hour**.
   - If a loop wants to act on a branch where `acting_on` is already set by another loop within the last hour, it must **skip** and log the collision.

2. **Separate state files**
   - `STATE.md` is the **global triage hub** (priorities, human inbox, cross-loop notes).
   - Each action loop uses its own state file:
     - `state.md` — primary builder loop
     - `<loop-name>-state.md` — additional loops
   - Loops MUST NOT write to other loops' state files.

3. **Triage reports, action loops execute**
   - Triage loops only **observe and schedule**.
   - Action loops implement code and run verifications.
   - Triage loops must never directly fix code; they assign work to action loops via `STATE.md`.

4. **Shared denylist**
   - Every loop shares the **same path denylist**:
     - `.git/`
     - `node_modules/`
     - `dist/`
     - `build/`
     - `coverage/`
     - binary assets (e.g., `.png`, `.jpg`, `.mp4`), unless the loop is explicitly about assets.
   - No loop is allowed to edit these paths unless its role explicitly requires it.

5. **Aggregate token budget**
   - All loops share a global token budget per day.
   - Each loop must respect its own budget slice and defer non-critical plans when close to budget limits.

---

## 2. State Layout

```text
STATE.md                    # Global triage (priorities, human inbox)
state.md                    # Primary builder loop
<loop-name>-state.md        # Additional action loops
loop-run-log.md             # Append-only observability
```

### STATE.md (global)

- Holds current priority list, Human Inbox, cross-loop notes and conflicts.
- Triage loops read and write this file.
- Action loops read it but write only status snippets about their domain.

### Per-loop state files

Each file must contain:

```markdown
## Loop Status
- acting_on: <branch-or-pr-id-or-null>
- last_run: <timestamp>
- last_result: <success|fail|skipped|noop>
- attempt_count: <number>
- notes: <short text>

## Queue / Items
- ...

## Log
- yyyy-mm-dd hh:mm — <summary>
```

### loop-run-log.md

- Append-only. Every loop writes a short line on each run:

```markdown
yyyy-mm-dd hh:mm — [loop-name] <action|skip|collision|noop> — details
```

---

## 3. Priority When Loops Conflict

| Priority | Loop               | Reason                          |
|----------|--------------------|---------------------------------|
| 1        | CI Sweeper         | Red main blocks everything      |
| 2        | Builder Loop       | Core development                |
| 3        | PR Babysitter      | Active PRs are time-sensitive   |
| 4        | Dependency Sweeper | Pause while CI red              |
| 5        | Post-Merge Cleanup | Off-peak, lowest urgency        |
| 6        | Daily Triage       | Reports only; schedules         |

Rules:

- CI Sweeper wins over all other loops for the same branch.
- Builder Loop yields to CI Sweeper if CI is red on its target branch.
- PR Babysitter yields if CI Sweeper or Builder Loop is already acting on the same PR or base branch.
- Dependency Sweeper runs only when main CI is **not red** and CI Sweeper is **not** currently acting on the same branch.
- Post-Merge Cleanup runs when CI is green or being actively fixed, with no direct collision with PR Babysitter.
- Daily Triage never overrides actions; it only creates TODOs in `STATE.md`.

---

## 4. Scheduler Coordination

```markdown
## Multi-loop schedule
- Builder Loop: /loop 30m (active hours)
- CI Sweeper: /loop 15m (active hours, if added)
- PR Babysitter: /loop 10m (active hours, skip if CI Sweeper acting on same PR)
- Daily Triage: /loop 1d 08:00
- Dependency Sweeper: /loop 6h (skip if main CI red)
- Post-Merge: /loop 1d 22:00
```

Guidelines:

- "Active hours" should match team working hours to avoid noisy commits at night.
- CI Sweeper and PR Babysitter should stagger (e.g., CI at :00/:15/:30/:45, PR at :05/:20/:35/:50).
- Daily Triage and Post-Merge prefer off-peak windows.

---

## 5. Collision Detection

Each action loop must implement collision detection before edits.

### Acting-on marker

- Each loop writes an `acting_on: branch-or-pr-id` field in its state file before editing or fixing.
- Before spawning a fix:

1. Read all other loop state files.
2. For each file:
   - If `acting_on` matches the current branch or PR id:
     - Check priority rules.
     - If another loop has higher or equal priority: skip action, log collision to `loop-run-log.md`, clear your own `acting_on`.
     - If you have higher priority: proceed but write a cross-loop note in `STATE.md`.

### Collision log example

```markdown
2026-06-28 12:05 — [pr-babysitter] collision — CI Sweeper already acting_on=main, skipping.
```

---

## 6. Human Inbox

Use a shared section in `STATE.md`:

```markdown
## Human Inbox (ambiguous / cross-loop)
- [ ] PR #42: CI Sweeper and PR Babysitter both flagged — human pick owner
- [ ] Dependency updates paused due to recurring CI failures — human decide priority
```

Rules:

- When loops conflict repeatedly on the same item for more than 3 runs, they must stop trying and add an entry to the Human Inbox.
- Triage loop can promote items from Human Inbox to specific loop queues.

---

## 7. Adding New Loops

When adding a new loop to this repo:

1. Create its state file (e.g., `ci-sweeper-state.md`).
2. Add its priority to the table in section 3.
3. Add its schedule to section 4.
4. Update `LOOP.md` to reference the new loop.
5. Test collision detection by running both loops against the same branch in a dry-run mode.

---

## 8. Loop Implementation Notes (for agents)

- All loops must respect **One owner per branch per hour**.
- Read `multiloop.md` before acting.
- Update their own state file every run.
- Append to `loop-run-log.md`.
- Use permissions to ensure triage agents cannot edit code and action agents cannot touch denylisted paths.

---

## 9. Current Active Loops

| Loop            | Level | Cadence | State File     | Status   |
|-----------------|-------|---------|----------------|----------|
| Builder Loop    | L2    | 30m     | `state.md`     | Active   |

All other loops are **inactive** until explicitly added via section 7.

---

*This file is a contract for loop behavior.
Every loop in this repository must follow these rules.*
