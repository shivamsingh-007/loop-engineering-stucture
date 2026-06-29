# tasks/todo.md — Task Plan & Progress

This file is the **task board** for AI agents working on the 3D Spider-Man comic project demo site.
Agents must update this file on every non-trivial loop iteration.

---

## 1. Current Goal

- Build a Spider-Man comic-themed 3D demo site with scroll-driven camera, project screenshots, and explainer video.

---

## 2. Active Tasks (Checklist)

### Step 1 — Base App Setup ✅

- [x] Initialize React app (Vite) and confirm dev server runs.
- [x] Configure base routing and root layout component.
- [x] Add placeholder sections (Hero, Projects, Screenshots, Demo, Video, Contact).
- [x] Document commands in `context.md`.

### Step 2 — Theme & Layout ✅

- [x] Implement global anime/comic theme (colors, typography, backgrounds).
- [x] Create section components in `src/components/sections/*`.
- [x] Ensure layout is responsive and visually coherent.
- [x] Add humor microcopy in Hero and Projects sections.

### Step 3 — 3D Scene Integration ✅

- [x] Install and configure React Three Fiber and Drei.
- [x] Add `<Canvas />` with base 3D scene and hero placeholder model.
- [x] Create `CameraRig` component for camera control.
- [x] Confirm scene renders smoothly on dev server.

### Step 4 — Scroll-Driven Camera ✅

- [x] Install and configure GSAP + ScrollTrigger.
- [x] Map scroll progress to camera position/rotation across sections.
- [x] Pin appropriate sections for cinematic transitions.
- [x] Verify motion is smooth and readable.

### Step 5 — Projects & Screenshots ✅

- [x] Implement project cards with humor and tech details.
- [x] Wire screenshot gallery with hover animations.
- [x] Connect project data to cards from a central config.
- [x] Ensure screenshots are lazy-loaded or optimized.

### Step 6 — Demo & Video ✅

- [x] Embed demo iframes or modal viewer for each main project.
- [x] Add explainer video section with player and fallback text.
- [x] Ensure layout does not break on different screen sizes.

### Step 7 — Polish & Verification ✅

- [x] Add micro-interactions (hover, focus, panel transitions).
- [x] Run tests and lint.
- [x] Run production build and fix blocking issues.
- [x] Capture final state in `state.md`.

### Spider-Man Redesign ✅

- [x] Spider-Man CSS theme (red/blue/black, web patterns, Bangers font)
- [x] Hero section with "THWIP!" sound effect and speech bubble
- [x] Living background with web strands, speed lines, particles
- [x] Comic panel cards with 3D hover tilt and web-glow
- [x] Web-shooter cursor effect
- [x] GSAP ScrollTrigger for all section reveals
- [x] External verifier confirmed ALL PASS

---

## 3. In-Progress Notes

- 2026-06-28 12:15 — [agent] Initial task list seeded; base app setup planned.
- 2026-06-28 12:30 — [agent] step-01 success — Vite+React+TS scaffolded.
- 2026-06-28 12:40 — [agent] step-02 success — CSS vars theme, panel styling.
- 2026-06-28 12:55 — [agent] step-03 success — R3F + Drei, 3D hero scene.
- 2026-06-28 13:05 — [agent] step-04 success — GSAP ScrollTrigger camera.
- 2026-06-28 13:15 — [agent] step-05 success — 4 project cards, gallery.
- 2026-06-28 13:25 — [agent] step-06 success — iframe demo, video player.
- 2026-06-28 13:30 — [agent] step-07 success — Final verification clean.
- 2026-06-29 — [agent] Spider-Man redesign complete. External verifier ALL PASS.

---

## 4. Review & Results

- Last iteration summary:
  - Step: step-spider-man-redesign
  - Result: success
  - Key changes: Complete Spider-Man comic theme with web patterns, THWIP effects, comic panels
  - Follow-up tasks: (backlog) Real demo URLs, code-split Three.js

---

## 5. Backlog / Future Ideas

- [ ] Add language toggle for copy.
- [ ] Add light/dark comic theme variant.
- [ ] Integrate analytics for demo usage.
