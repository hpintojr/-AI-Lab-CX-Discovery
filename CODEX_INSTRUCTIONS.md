# CODEX EXECUTION INSTRUCTIONS (`CodexGPT 6.1 Sol` - Medium)

Welcome Codex! Everything in this repository (`hpintojr/-AI-Lab-CX-Discovery`) has been pre-scaffolded to match the exact layout template of **`hpintojr/button-bear-ai-lab`** and the **`/MCX-AI-Labs/data-financial-analysis`** portfolio template in `hpintojr/hpintojr`.

## YOUR 3 TASKS WHEN HAMILTON SAYS "LOOK AT THE REPO & RUN"

### TASK 1: Start the Local Webapp Server
Run the static server from the `public/` folder so the full interactive dashboard, teleprompter script, and downloads are live:
```bash
python3 -m http.server 8766 --directory public &
```
Open `http://localhost:8766/` in the desktop browser.

### TASK 2: Human-Paced Screen Recording Walkthrough (For Hamilton's Video Edit)
Hamilton is recording his screen and will speed-ramp the footage in post-production. Follow these pacing rules strictly:
1. **Pause 2 to 3 seconds** between clicks, tab switches, and smooth scrolls.
2. **Human Typing with Realistic Mistakes (For Short Inputs):**
   When demonstrating the skill setup (`ux-persona-builder`) and initial prompts (`prompts/all_11_steps_prompts.md`), type at ~65 WPM (70–130ms per key) using `scripts/human_typer.py` (or `xdotool`):
   - **Typo 1 (Skill Name):** Type `ux-presona` -> pause 0.35s -> press Backspace 6 times -> type `ersona-builder`.
   - **Typo 2 (Prompt 1 Converge):** Type `Identfiy the most obviosu ` -> pause 0.35s -> press Backspace 8 times -> type `obvious customer persona and use case...`
   - **Typo 3 (Prompt 2 Diverge):** Type `Look past the domniant ` -> pause 0.35s -> press Backspace 6 times -> type `minant pattern for a non-obvious B2B persona...`
3. **Smart Paste for Large Data Blocks:**
   When loading `public/files/Mercury_CRM_Market_Packet.txt` or the full skill markdown (`public/files/ux-persona-builder-skill.md`), copy to clipboard, pause 1.5s, paste (`Ctrl+V`), and pause 2s.
4. **Interactive Dashboard Walkthrough on Screen:**
   In the browser at `http://localhost:8766/`, smoothly click through all 5 tabs in order, pausing 4–5 seconds on each tab and scrolling smoothly from top to bottom:
   - Tab 1: **Decision** (`/?tab=decision`) — Show the 4 KPI cards (`65.0%` DIY trial drop-off, `5–20x` agency multiplier, `95.0%` tool-first failure rate, `30 / 70` build vs. adoption split) and the 2 comparison charts.
   - Tab 2: **Personas & scenarios** (`/?tab=personas`) — Show the `ux-persona-builder` skill card, the 4 Persona Cards (*Speed-to-Lead Sam*, *Field-Crew Carlos*, *Agency Architect Alex*, and *Freebie-Hunter Sid*), and the Step 5 Concrete Scenarios table.
   - Tab 3: **Usability & 40-buyer panel** (`/?tab=testing`) — Show the Step 7 section-by-section walkthrough, the 80/20 Pareto friction stack-rank, the Survey Bias Self-Critique, and the 40-respondent synthetic panel results.
   - Tab 4: **CRO split test & ideation** (`/?tab=splittest`) — Show Variant A (14-Day Free DIY Trial) vs. Variant B (60-Second Live AI Call + 5-Day Revenue Diagnostic), the 8 product ideas, and the Step 11 DVF Scorecard + Steelman Objection.
   - Tab 5: **Brief & verification** (`/?tab=evidence`) — Show the Step 6 Evidence Linter Claims Register and verification record.
   - Finally, click **Recording script** (`/script/`) and **Downloads** (`/downloads/`) in the top navbar.

### TASK 3: Sync with Main Portfolio (`hpintojr/hpintojr` -> `/MCX-AI-Labs`)
If the sibling repo `hpintojr` is cloned locally:
1. Copy the pre-built Lab 03 JSON object from `portfolio_sync/lab03_entry.json` into `scripts/mcx-ai-labs/labs.json` (replacing the `"upcoming"` entry for `"slug": "synthetic-research-cx-discovery"`).
2. Run:
   ```bash
   node scripts/mcx-ai-labs/build.mjs
   ```
   This updates `public/MCX-AI-Labs/index.html` to **3 of 12 complete · 25%** and builds `public/MCX-AI-Labs/synthetic-research-cx-discovery/index.html` using the exact `data-financial-analysis` template.
