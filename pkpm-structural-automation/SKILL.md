---
name: pkpm-structural-automation
description: Automate and guide Windows desktop workflows for PKPM structural engineering calculations, including model backup, project opening, PMCAD/SATWE/PKPM modules, parameter entry, calculation runs, result extraction, error triage, and deliverable packaging. Use when Codex is asked to operate a computer, remote desktop, GUI automation tool, screenshots, OCR, scripts, or runbooks to complete PKPM structure calculation tasks.
---

# PKPM Structural Automation

Use this skill to help a user complete PKPM structural calculation work on a Windows desktop through GUI automation, scripted runbooks, or step-by-step operator guidance.

## Safety and responsibility boundaries

- Treat PKPM output as engineering-analysis support, not a final professional judgment.
- Ask the user to confirm project path, PKPM version, code/standard, structure type, design stage, and expected deliverables before changing files.
- Never overwrite the original model. Create a timestamped backup before opening or calculating.
- Do not silently accept warnings, model changes, parameter defaults, or failed checks. Record them in the run log and ask the user when engineering judgment is required.
- Do not perform unattended destructive desktop actions. If a GUI action could delete, overwrite, submit, or irreversibly update a model, pause and request confirmation.
- Keep screenshots, logs, exported reports, and modified PKPM files organized under a session folder.

## Decide the execution mode

1. **GUI automation mode**: Use when the environment provides desktop-control tools, screenshots, OCR, keyboard/mouse input, or a live Windows session with PKPM installed.
2. **Runbook mode**: Use when no GUI control is available. Generate a precise operator checklist using `scripts/pkpm_runbook.py`, then guide the user through PKPM manually.
3. **Artifact review mode**: Use when the user provides PKPM reports, calculation logs, screenshots, or exported text/PDF/DWG files. Extract warnings, summarize checks, and identify items needing engineering review.

## Standard workflow

1. **Collect inputs**
   - Project folder and model name.
   - PKPM version/module names available on the machine.
   - Building information: structural system, number of stories, seismic intensity/group, site category, design code, wind/seismic parameters, material strengths, load assumptions, and design stage.
   - Required outputs: calculation book, SATWE result tables, reinforcement drawings, warning list, PDF package, or review memo.
2. **Prepare a session**
   - Create a session folder named `pkpm_session_<project>_<YYYYMMDD_HHMMSS>`.
   - Copy the source model into `backup_original/` before launching PKPM.
   - Start a run log with operator, time, PKPM version, source path, backup path, and requested outputs.
3. **Open and verify the model**
   - Launch PKPM from the Start menu, desktop shortcut, or known executable.
   - Open the copied model, not the original.
   - Confirm story count, axes/grids, standard floors, materials, loads, and model integrity before calculation.
4. **Set calculation parameters**
   - Compare PKPM defaults with user-provided design assumptions.
   - Capture screenshots of important parameter dialogs.
   - Record every changed parameter in the run log.
5. **Run calculations**
   - Run the requested PKPM modules in dependency order, commonly model/preprocessing first, then SATWE structural analysis/design, then reinforcement/drawing or report exports.
   - Monitor progress dialogs and logs until completion.
   - If an error dialog appears, capture the screenshot, record the exact message, stop the run, and triage before retrying.
6. **Extract and check results**
   - Export calculation results and text reports where possible.
   - Review warnings and failed checks first, then displacement/drift, period ratio, shear-weight ratio, axial compression ratio, stiffness irregularity, story shear, reinforcement limits, and any project-specific checks.
   - Distinguish software execution success from engineering compliance.
7. **Package deliverables**
   - Save exported reports, screenshots, run log, warning summary, and final model copy under the session folder.
   - Provide a concise summary: inputs used, modules run, outputs generated, warnings/errors, assumptions changed, and items requiring engineer confirmation.

## GUI automation practices

- Prefer stable UI anchors: window titles, menu text, dialog labels, and OCR text over absolute coordinates.
- Before clicking, inspect the active window/screenshot and verify the target control.
- Use conservative waits for PKPM calculations; long-running structural solves can appear idle while processing.
- Capture a screenshot before and after every major stage: project open, parameter dialogs, calculation completion, error/warning dialogs, and export dialogs.
- Keep a plain-language action log such as `HH:MM:SS opened copied model`, `HH:MM:SS changed seismic intensity to ...`, `HH:MM:SS SATWE completed with warnings`.
- If PKPM displays ambiguous Chinese prompts such as overwrite, synchronize model, repair database, continue with errors, or update parameters, pause and ask the user unless the expected choice was already documented.

## Use bundled resources

- Use `references/pkpm_workflow.md` for the detailed checklist and result-review categories.
- Use `scripts/pkpm_runbook.py` to create a session runbook when GUI automation is unavailable or before starting a live PKPM session.

Example:

```bash
python scripts/pkpm_runbook.py \
  --project-name "办公楼结构" \
  --project-path "D:\\PKPM\\Projects\\Office" \
  --pkpm-version "PKPM V6" \
  --structure-type "框架-剪力墙" \
  --deliverable "SATWE计算书" \
  --deliverable "警告汇总" \
  --output pkpm_runbook.md
```
