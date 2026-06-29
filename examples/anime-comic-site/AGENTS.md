# AGENTS.md — Spider-Man Comic Demo Site

This file configures AI agents for the **3D Spider-Man Comic Demo Site**.
It is a **companion** to `loop-rules.md`, which is the global loop constitution.

---

## Loop Discipline

This project follows the global loop rules in `loop-rules.md`.
If any instruction here conflicts with `loop-rules.md`, the rules in `loop-rules.md` win.

Agents must:
- Read `loop-rules.md` on every new session.
- Obey its PLAN → IMPLEMENT → VERIFY order.
- Use the verifier configuration below to satisfy the "separate checker" requirement.

---

## Project Summary

- **Goal**: Build a Spider-Man comic-themed 3D demo site.
- **Stack**: React 19, Vite, TypeScript, React Three Fiber, Drei, GSAP + ScrollTrigger.
- **Theme**: Red/blue/black palette, Bangers font, web patterns, "THWIP!" effects, comic panels.

---

## Tech Stack & Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start Vite dev server (localhost:5173) |
| `npm run build` | Production build (`tsc -b && vite build`) |
| `npm run lint` | Type check (`tsc --noEmit`) |
| `npx tsc --noEmit` | TypeScript check only |

Agents must run at least `npm run build` and `npx tsc --noEmit` before marking a step verified.

---

## Verifier Configuration

This project uses an **external verifier agent** for the VERIFY phase.

**Current setup:**
- Provider: OpenRouter API
- Model: `nvidia/nemotron-3-super-120b-a12b:free` (or available free model)
- API Key: Stored in environment variable `OPENROUTER_API_KEY`

**Fallback:**
- If OpenRouter is unavailable (rate limit, timeout):
  - Mark step as `[!] verification_pending` in `tasks/todo.md`.
  - Do NOT mark as `[x] completed`.
  - Retry verification when available.

**Verifier prompt pattern:**
```
You are a build verification agent. Reply ONLY with a JSON object.
Check these items and mark PASS or FAIL:
1. Build passed (exit code 0)
2. TypeScript clean (no errors)
3. Spider-Man theme intact (CSS variables, Bangers font, web patterns)
4. GSAP ScrollTrigger functional
5. 3D scene renders without errors
Output: {"checks": [{"name": "...", "status": "PASS" or "FAIL"}]}
```

---

## Subagent Strategy

Use subagents to keep the main agent focused:

- One task per subagent.
- Subagents return findings only (no file edits unless allowed).
- Main agent coordinates and integrates.

---

## Self-Improvement

- After ANY correction: add lesson to `tasks/lessons.md`.
- Before PLAN: read relevant lessons.
- Apply lessons to avoid repeating mistakes.

---

## Core Principles

- **Simplicity First**: Minimal changes, avoid unnecessary refactors.
- **No Laziness**: Find root causes, no temporary fixes.
- **Minimal Impact**: Touch only what's necessary.

---

*This file is project-specific. For loop shape and discipline, see `loop-rules.md`.*
