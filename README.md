# Loop Engineering Structure

A reusable, project-agnostic loop engineering framework for AI coding agents.
Drop these files into any repo to get structured, autonomous PLAN → IMPLEMENT → VERIFY loops.

---

## What Is This?

Loop engineering is a pattern for AI coding agents where work is broken into small, verifiable steps. The agent:

1. **Plans** the next step.
2. **Implements** code changes.
3. **Verifies** the result (internal checks + external verifier).
4. **Decides** to retry or advance.
5. **Updates** state and commits.
6. **Repeats** until the goal is achieved.

This framework provides the global rules, execution algorithm, coordination rules, and templates you need to set this up in any project.

---

## File Roles

### Global Core (copy as-is to any repo)

| File | Role |
|------|------|
| `loop-rules.md` | Global constitution — non-negotiable rules for all agents |
| `AGENT_LOOP.md` | Detailed execution algorithm — the loop phases and logic |
| `multiloop.md` | Multi-loop coordination — priorities, collision detection, denylist |
| `STATE.md` | Global triage — cross-loop priorities and human inbox |
| `loop-run-log.md` | Append-only run history — observability across all loops |

### Project-Specific (instantiate from templates)

| File | Role |
|------|------|
| `AGENTS.md` | Agent config — verifier setup, tech stack, commands |
| `LOOP.md` | Loop definitions — which loops exist, step breakdown, cadence |
| `context.md` | Project description — goals, architecture, conventions |
| `state.md` | Per-loop state — current step, attempts, log |
| `tasks/todo.md` | Task board — checkable items with success criteria |
| `tasks/lessons.md` | Self-improvement — mistake patterns and rules to avoid |

---

## How to Port to a New Repo

### Step 1: Copy Global Files

Copy these files to the root of your target repo:

```
loop-rules.md
AGENT_LOOP.md
multiloop.md
STATE.md
loop-run-log.md
```

### Step 2: Instantiate Templates

Copy from `templates/` and fill in project-specific content:

```
templates/AGENTS.md.template      → AGENTS.md
templates/LOOP.md.template        → LOOP.md
templates/context.md.template     → context.md
templates/state.md.template       → state.md
templates/loop-run-log.md.template → loop-run-log.md
templates/tasks/todo.md.template  → tasks/todo.md
templates/tasks/lessons.md.template → tasks/lessons.md
```

### Step 3: Configure Your Verifier

In `AGENTS.md`, fill in:
- Which provider/model you'll use for external verification.
- API key environment variable.
- Project-specific verification checks.

### Step 4: Define Your Steps

In `LOOP.md`, define:
- What steps make up your project.
- What success criteria each step has.
- What commands to run for verification.

### Step 5: Start the Loop

Once everything is set up:

1. Give the agent a GOAL.
2. The agent reads `loop-rules.md` and all context files.
3. The agent plans the first step.
4. The agent implements, verifies, and commits.
5. Repeat until done.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                  loop-rules.md                  │
│         (global constitution, same in all repos)│
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────┐│
│  │ AGENT_LOOP  │  │  multiloop  │  │ STATE.md││
│  │   .md       │  │    .md      │  │         ││
│  │ (execution) │  │ (multi-loop)│  │ (triage)││
│  └─────────────┘  └─────────────┘  └─────────┘│
│                                                 │
├─────────────────────────────────────────────────┤
│              Project-Specific Layer             │
│                                                 │
│  ┌───────────┐  ┌──────────┐  ┌──────────────┐│
│  │ AGENTS.md │  │ LOOP.md  │  │  context.md  ││
│  │ (verifier │  │ (steps)  │  │  (goals,     ││
│  │  config)  │  │          │  │   stack)     ││
│  └───────────┘  └──────────┘  └──────────────┘│
│                                                 │
│  ┌───────────┐  ┌──────────┐  ┌──────────────┐│
│  │ state.md  │  │ tasks/*  │  │loop-run-log  ││
│  │ (status)  │  │ (plans)  │  │  .md (log)   ││
│  └───────────┘  └──────────┘  └──────────────┘│
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Quickstart

```bash
# 1. Clone this repo (or copy the files)
git clone https://github.com/shivamsingh-007/loop-engineering-stucture.git

# 2. Copy global files to your target repo
cp loop-rules.md AGENT_LOOP.md multiloop.md STATE.md loop-run-log.md /path/to/your/repo/

# 3. Copy and fill templates
cp templates/AGENTS.md.template /path/to/your/repo/AGENTS.md
cp templates/LOOP.md.template /path/to/your/repo/LOOP.md
cp templates/context.md.template /path/to/your/repo/context.md
cp templates/state.md.template /path/to/your/repo/state.md
mkdir -p /path/to/your/repo/tasks
cp templates/tasks/todo.md.template /path/to/your/repo/tasks/todo.md
cp templates/tasks/lessons.md.template /path/to/your/repo/tasks/lessons.md

# 4. Edit AGENTS.md with your verifier config
# 5. Edit LOOP.md with your step breakdown
# 6. Edit context.md with your project description
# 7. Start your agent with a GOAL
```

---

## Loop Shape

```
TRIGGER (goal assigned)
    │
    ▼
┌─────────┐     ┌────────────┐     ┌─────────┐
│  PLAN   │────▶│  IMPLEMENT │────▶│  VERIFY │
└─────────┘     └────────────┘     └─────────┘
    ▲                                   │
    │           ┌────────────┐          │
    └───────────│   DECIDE   │◀─────────┘
                │  (retry or │
                │   advance) │
                └─────┬──────┘
                      │
                      ▼
              ┌──────────────┐
              │ UPDATE STATE │
              │   & COMMIT   │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │ REPEAT / STOP│
              └──────────────┘
```

---

## Multi-Loop Support

When running multiple loops (e.g., Builder + CI Sweeper + PR Babysitter):

- Each loop has its own state file.
- `STATE.md` is the shared triage hub.
- `loop-run-log.md` records all activity.
- Collision detection uses `acting_on` markers.
- Priority ordering prevents conflicts.

See `multiloop.md` for full coordination rules.

---

## Examples

The `examples/` directory contains a filled-in example showing this framework applied to a concrete project (Spider-Man comic 3D demo site). Use it as reference when setting up your own project.

---

## License

This framework is provided as-is. Use it in any project.
