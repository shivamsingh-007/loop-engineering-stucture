<div align="center">

<!-- Hero Banner SVG -->
<svg width="600" height="180" viewBox="0 0 600 180" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="600" height="180" rx="16" fill="#FFFBF0"/>
  <rect width="600" height="180" rx="16" stroke="#D4A574" stroke-width="2"/>
  
  <!-- Loop Icon -->
  <g transform="translate(80, 90)">
    <!-- Circular arrow -->
    <circle cx="0" cy="0" r="45" fill="none" stroke="#FF8C42" stroke-width="4" stroke-dasharray="20 10"/>
    <polygon points="40,-20 55,-10 40,0" fill="#FF8C42"/>
    <circle cx="0" cy="0" r="35" fill="#FFE066" opacity="0.3"/>
    <text x="0" y="8" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#2D2D2D">L-E</text>
  </g>
  
  <!-- Title -->
  <text x="170" y="75" font-family="Georgia, serif" font-size="32" font-weight="bold" fill="#2D2D2D">Loop Engineering</text>
  <text x="170" y="105" font-family="Georgia, serif" font-size="22" fill="#D4A574">Structure</text>
  
  <!-- Tagline -->
  <text x="170" y="135" font-family="monospace" font-size="12" fill="#666666">PLAN → IMPLEMENT → VERIFY → repeat</text>
  
  <!-- Badge -->
  <rect x="170" y="148" width="120" height="22" rx="4" fill="#FFE066"/>
  <text x="230" y="163" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#2D2D2D">FRAMEWORK</text>
</svg>

<br/>

**A reusable loop engineering framework for AI coding agents.**

Drop these files into any repo → get structured, autonomous PLAN → IMPLEMENT → VERIFY loops.

<br/>

[![Framework](https://img.shields.io/badge/Status-Complete-green?style=flat-square)](https://github.com/shivamsingh-007/loop-engineering-stucture)
[![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)](#license)

</div>

---

## What Is This?

Loop engineering is a pattern where AI coding agents work in **small, verifiable steps** instead of trying to do everything at once. The agent:

1. **Plans** one step (small, testable, with clear success criteria)
2. **Implements** the code changes
3. **Verifies** the result (internal checks + external verifier)
4. **Decides** to retry or advance to the next step
5. **Updates** state and commits
6. **Repeats** until the goal is achieved

This framework gives you the rules, algorithms, coordination logic, and templates to set this up in **any project** — frontend, backend, data, infra, mobile, CLI.

---

## The Loop Flow

<!-- Loop Flow SVG -->
<svg width="100%" height="280" viewBox="0 0 580 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="580" height="280" rx="12" fill="#FFFBF0"/>
  <rect width="580" height="280" rx="12" stroke="#D4A574" stroke-width="1"/>
  
  <!-- Trigger -->
  <rect x="200" y="10" width="180" height="40" rx="8" fill="#FFE066"/>
  <text x="290" y="35" text-anchor="middle" font-family="monospace" font-size="12" font-weight="bold" fill="#2D2D2D">TRIGGER (goal)</text>
  <line x1="290" y1="50" x2="290" y2="70" stroke="#D4A574" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- PLAN -->
  <rect x="40" y="75" width="130" height="50" rx="10" fill="#FF8C42"/>
  <text x="105" y="105" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#FFFFFF">PLAN</text>
  
  <!-- Arrow PLAN → IMPLEMENT -->
  <line x1="170" y1="100" x2="210" y2="100" stroke="#D4A574" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- IMPLEMENT -->
  <rect x="215" y="75" width="140" height="50" rx="10" fill="#D4A574"/>
  <text x="285" y="105" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#FFFFFF">IMPLEMENT</text>
  
  <!-- Arrow IMPLEMENT → VERIFY -->
  <line x1="355" y1="100" x2="395" y2="100" stroke="#D4A574" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- VERIFY -->
  <rect x="400" y="75" width="140" height="50" rx="10" fill="#FCA5A5"/>
  <text x="470" y="105" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#2D2D2D">VERIFY</text>
  
  <!-- Arrow VERIFY → DECIDE -->
  <line x1="470" y1="125" x2="470" y2="155" stroke="#D4A574" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- DECIDE -->
  <rect x="200" y="160" width="180" height="50" rx="10" fill="#FFE066"/>
  <text x="290" y="190" text-anchor="middle" font-family="monospace" font-size="14" font-weight="bold" fill="#2D2D2D">DECIDE</text>
  <text x="290" y="205" text-anchor="middle" font-family="monospace" font-size="9" fill="#666666">(retry or advance)</text>
  
  <!-- Arrow DECIDE → back to PLAN -->
  <path d="M200,185 L105,185 L105,125" fill="none" stroke="#FF8C42" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrow-orange)"/>
  
  <!-- Arrow DECIDE → UPDATE -->
  <line x1="290" y1="210" x2="290" y2="230" stroke="#D4A574" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- UPDATE & COMMIT -->
  <rect x="170" y="235" width="240" height="35" rx="8" fill="#FF8C42"/>
  <text x="290" y="257" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#FFFFFF">UPDATE STATE &amp; COMMIT</text>
  
  <!-- Arrow back to PLAN (repeat) -->
  <path d="M170,252 L40,252 L40,100" fill="none" stroke="#FF8C42" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrow-orange)"/>
  <text x="25" y="180" font-family="monospace" font-size="9" fill="#FF8C42" transform="rotate(-90, 25, 180)">REPEAT</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#D4A574"/>
    </marker>
    <marker id="arrow-orange" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#FF8C42"/>
    </marker>
  </defs>
</svg>

---

## File Roles

### Global Core (copy as-is to any repo)

These files are **project-agnostic** — they work the same everywhere:

| File | Role | Reusable? |
|------|------|-----------|
| `loop-rules.md` | Global constitution — non-negotiable rules for all agents | ✅ Same in every repo |
| `AGENT_LOOP.md` | Execution algorithm — the loop phases and logic | ✅ Same in every repo |
| `multiloop.md` | Multi-loop coordination — priorities, collision detection | ✅ Same in every repo |
| `STATE.md` | Global triage — cross-loop priorities and human inbox | ✅ Same structure |
| `loop-run-log.md` | Append-only run history — observability | ✅ Same format |

### Project-Specific (instantiate from templates)

These files get **customized** for each project:

| File | Role | Reusable? |
|------|------|-----------|
| `AGENTS.md` | Agent config — verifier setup, tech stack, commands | ❌ Project-specific |
| `LOOP.md` | Loop definitions — step breakdown, cadence | ❌ Project-specific |
| `context.md` | Project description — goals, architecture, conventions | ❌ Project-specific |
| `state.md` | Per-loop state — current step, attempts, log | ❌ Project-specific |
| `tasks/todo.md` | Task board — checkable items with success criteria | ❌ Project-specific |
| `tasks/lessons.md` | Self-improvement — mistake patterns | ❌ Project-specific |

---

## Architecture

<!-- Architecture SVG -->
<svg width="100%" height="350" viewBox="0 0 500 350" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="500" height="350" rx="12" fill="#FFFBF0"/>
  <rect width="500" height="350" rx="12" stroke="#D4A574" stroke-width="1"/>
  
  <!-- Global Layer Label -->
  <text x="250" y="25" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#FF8C42">GLOBAL LAYER (same in every repo)</text>
  
  <!-- Global Layer Background -->
  <rect x="20" y="35" width="460" height="110" rx="8" fill="#FFE066" opacity="0.3"/>
  <rect x="20" y="35" width="460" height="110" rx="8" stroke="#FF8C42" stroke-width="2" stroke-dasharray="6 3"/>
  
  <!-- Global Files -->
  <rect x="35" y="50" width="120" height="40" rx="6" fill="#FF8C42"/>
  <text x="95" y="75" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#FFFFFF">loop-rules.md</text>
  
  <rect x="170" y="50" width="120" height="40" rx="6" fill="#FF8C42"/>
  <text x="230" y="75" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#FFFFFF">AGENT_LOOP.md</text>
  
  <rect x="305" y="50" width="100" height="40" rx="6" fill="#FF8C42"/>
  <text x="355" y="75" text-anchor="middle" font-family="monospace" font-size="10" font-weight="bold" fill="#FFFFFF">multiloop.md</text>
  
  <rect x="50" y="100" width="90" height="35" rx="6" fill="#D4A574"/>
  <text x="95" y="122" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFFFFF">STATE.md</text>
  
  <rect x="160" y="100" width="140" height="35" rx="6" fill="#D4A574"/>
  <text x="230" y="122" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFFFFF">loop-run-log.md</text>
  
  <rect x="320" y="100" width="100" height="35" rx="6" fill="#FCA5A5"/>
  <text x="370" y="122" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">README.md</text>
  
  <!-- Divider -->
  <line x1="30" y1="155" x2="470" y2="155" stroke="#D4A574" stroke-width="2"/>
  
  <!-- Project Layer Label -->
  <text x="250" y="175" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#D4A574">PROJECT-SPECIFIC LAYER (customized per repo)</text>
  
  <!-- Project Layer Background -->
  <rect x="20" y="185" width="460" height="150" rx="8" fill="#D4A574" opacity="0.15"/>
  <rect x="20" y="185" width="460" height="150" rx="8" stroke="#D4A574" stroke-width="1"/>
  
  <!-- Project Files Row 1 -->
  <rect x="35" y="200" width="100" height="35" rx="6" fill="#D4A574"/>
  <text x="85" y="222" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFFFFF">AGENTS.md</text>
  
  <rect x="150" y="200" width="90" height="35" rx="6" fill="#D4A574"/>
  <text x="195" y="222" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFFFFF">LOOP.md</text>
  
  <rect x="255" y="200" width="100" height="35" rx="6" fill="#D4A574"/>
  <text x="305" y="222" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFFFFF">context.md</text>
  
  <rect x="370" y="200" width="90" height="35" rx="6" fill="#FFE066"/>
  <text x="415" y="222" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">state.md</text>
  
  <!-- Project Files Row 2 -->
  <rect x="50" y="250" width="130" height="35" rx="6" fill="#FFE066"/>
  <text x="115" y="272" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">tasks/todo.md</text>
  
  <rect x="200" y="250" width="140" height="35" rx="6" fill="#FFE066"/>
  <text x="270" y="272" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">tasks/lessons.md</text>
  
  <rect x="360" y="250" width="100" height="35" rx="6" fill="#FCA5A5" opacity="0.7"/>
  <text x="410" y="272" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">templates/*</text>
  
  <!-- Legend -->
  <rect x="35" y="295" width="12" height="12" rx="2" fill="#FF8C42"/>
  <text x="52" y="305" font-family="monospace" font-size="9" fill="#666666">= Global core</text>
  
  <rect x="150" y="295" width="12" height="12" rx="2" fill="#D4A574"/>
  <text x="167" y="305" font-family="monospace" font-size="9" fill="#666666">= Project config</text>
  
  <rect x="280" y="295" width="12" height="12" rx="2" fill="#FFE066"/>
  <text x="297" y="305" font-family="monospace" font-size="9" fill="#666666">= State/tasks</text>
  
  <rect x="395" y="295" width="12" height="12" rx="2" fill="#FCA5A5"/>
  <text x="412" y="305" font-family="monospace" font-size="9" fill="#666666">= Templates</text>
</svg>

---

## How to Port to a New Repo

### Step 1: Copy Global Files

Copy these 5 files to your target repo root:

```
loop-rules.md
AGENT_LOOP.md
multiloop.md
STATE.md
loop-run-log.md
```

### Step 2: Instantiate Templates

Fill in project-specific content:

```
templates/AGENTS.md.template        →  AGENTS.md
templates/LOOP.md.template          →  LOOP.md
templates/context.md.template       →  context.md
templates/state.md.template         →  state.md
templates/loop-run-log.md.template  →  loop-run-log.md
templates/tasks/todo.md.template    →  tasks/todo.md
templates/tasks/lessons.md.template →  tasks/lessons.md
```

### Step 3: Configure Your Verifier

In `AGENTS.md`, fill in:
- Provider/model for external verification
- API key environment variable
- Project-specific verification checks

### Step 4: Define Your Steps

In `LOOP.md`, define:
- What steps make up your project
- Success criteria for each step
- Commands to run for verification

### Step 5: Start the Loop

1. Give the agent a **GOAL**
2. Agent reads `loop-rules.md` and all context files
3. Agent plans the first step
4. Agent implements, verifies, and commits
5. Repeat until done

---

## Multi-Loop Coordination

<!-- Multi-Loop SVG -->
<svg width="100%" height="200" viewBox="0 0 500 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="500" height="200" rx="12" fill="#FFFBF0"/>
  <rect width="500" height="200" rx="12" stroke="#D4A574" stroke-width="1"/>
  
  <!-- Title -->
  <text x="250" y="25" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#2D2D2D">MULTI-LOOP COORDINATION</text>
  
  <!-- STATE.md Hub -->
  <rect x="190" y="80" width="120" height="40" rx="8" fill="#FF8C42"/>
  <text x="250" y="105" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#FFFFFF">STATE.md</text>
  <text x="250" y="72" text-anchor="middle" font-family="monospace" font-size="9" fill="#666666">(triage hub)</text>
  
  <!-- Builder Loop -->
  <rect x="30" y="140" width="100" height="35" rx="6" fill="#D4A574"/>
  <text x="80" y="162" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFFFFF">Builder Loop</text>
  <line x1="130" y1="150" x2="190" y2="110" stroke="#D4A574" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- CI Sweeper -->
  <rect x="200" y="140" width="100" height="35" rx="6" fill="#FCA5A5"/>
  <text x="250" y="162" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">CI Sweeper</text>
  <line x1="250" y1="140" x2="250" y2="120" stroke="#FCA5A5" stroke-width="2" marker-end="url(#arrow-red)"/>
  
  <!-- PR Babysitter -->
  <rect x="370" y="140" width="100" height="35" rx="6" fill="#FFE066"/>
  <text x="420" y="162" text-anchor="middle" font-family="monospace" font-size="9" fill="#2D2D2D">PR Babysitter</text>
  <line x1="370" y1="150" x2="310" y2="110" stroke="#FFE066" stroke-width="2" marker-end="url(#arrow-yellow)"/>
  
  <!-- Collision Warning -->
  <text x="250" y="195" text-anchor="middle" font-family="monospace" font-size="9" fill="#FCA5A5">⚠ One owner per branch per hour</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrow-red" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#FCA5A5"/>
    </marker>
    <marker id="arrow-yellow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0,0 8,3 0,6" fill="#FFE066"/>
    </marker>
  </defs>
</svg>

When running multiple loops:

- Each loop has its own state file
- `STATE.md` is the shared triage hub
- `loop-run-log.md` records all activity
- Collision detection uses `acting_on` markers
- Priority ordering prevents conflicts

See `multiloop.md` for full coordination rules.

---

## Example

The `examples/anime-comic-site/` directory shows this framework applied to a real project:

| File | What it shows |
|------|---------------|
| `AGENTS.md` | Configured for a Spider-Man 3D demo site |
| `state.md` | 9 completed steps with full log |
| `tasks/todo.md` | Real task board with success criteria |
| `tasks/lessons.md` | 5 lessons learned during development |

Use it as a reference when setting up your own project.

---

## Quickstart

```bash
# 1. Clone this repo
git clone https://github.com/shivamsingh-007/loop-engineering-stucture.git

# 2. Copy global files to your project
cp loop-engineering-stucture/loop-rules.md your-project/
cp loop-engineering-stucture/AGENT_LOOP.md your-project/
cp loop-engineering-stucture/multiloop.md your-project/
cp loop-engineering-stucture/STATE.md your-project/
cp loop-engineering-stucture/loop-run-log.md your-project/

# 3. Copy and customize templates
cp loop-engineering-stucture/templates/AGENTS.md.template your-project/AGENTS.md
cp loop-engineering-stucture/templates/LOOP.md.template your-project/LOOP.md
cp loop-engineering-stucture/templates/context.md.template your-project/context.md
cp loop-engineering-stucture/templates/state.md.template your-project/state.md

# 4. Set up tasks directory
mkdir -p your-project/tasks
cp loop-engineering-stucture/templates/tasks/todo.md.template your-project/tasks/todo.md
cp loop-engineering-stucture/templates/tasks/lessons.md.template your-project/tasks/lessons.md

# 5. Edit AGENTS.md → configure your verifier
# 6. Edit LOOP.md → define your steps
# 7. Edit context.md → describe your project
# 8. Give your agent a GOAL and watch it loop
```

---

## License

This framework is provided as-is. Use it in any project.
