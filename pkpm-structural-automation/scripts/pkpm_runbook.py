#!/usr/bin/env python3
"""Generate a PKPM structural calculation runbook markdown file."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def build_runbook(args: argparse.Namespace) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    deliverables = "\n".join(f"- [ ] {item}" for item in args.deliverable) or "- [ ] Calculation report"
    assumptions = "\n".join(f"- {item}" for item in args.assumption) or "- None recorded yet."
    return f"""# PKPM Structural Calculation Runbook

Generated: {timestamp}

## Project

- Project name: {args.project_name}
- Project path: `{args.project_path}`
- PKPM version: {args.pkpm_version}
- Structure type: {args.structure_type}
- Design code/standard: {args.design_code}

## Required deliverables

{deliverables}

## Known assumptions

{assumptions}

## Session setup

- [ ] Create session folder: `pkpm_session_{safe_name(args.project_name)}_<YYYYMMDD_HHMMSS>`.
- [ ] Copy the source model into `backup_original/`.
- [ ] Open only the copied model in PKPM.
- [ ] Record PKPM version, operator, source path, backup path, and start time.

## Pre-run model verification

- [ ] Confirm story count, story heights, axes/grids, and standard floor mapping.
- [ ] Confirm member sections, materials, slab openings, constraints, transfer stories, and basements.
- [ ] Confirm gravity, wind, seismic, equipment, roof, and special load assumptions.
- [ ] Capture screenshots of key model and parameter dialogs.

## Calculation sequence

- [ ] Run model/preprocessing checks.
- [ ] Generate analysis data for SATWE or the requested PKPM analysis module.
- [ ] Run structural analysis and design.
- [ ] Capture completion dialog or error/warning dialog screenshots.
- [ ] Export result tables, calculation book, warning list, and drawings/reports.

## Result review

- [ ] Fatal errors and warning messages.
- [ ] Periods, period ratio, mass participation, base shear, and shear-weight ratio.
- [ ] Displacement/drift, torsional irregularity, stiffness ratio, weak/soft story indicators.
- [ ] Member axial compression ratio, capacity warnings, reinforcement limits, and overstress items.
- [ ] Deliverable completeness and consistency with final calculated model.

## Pause conditions

Pause for user confirmation if PKPM asks to repair, synchronize, upgrade, overwrite, rebuild data, continue after errors, or accept unknown parameter defaults.
"""


def safe_name(value: str) -> str:
    return "".join(char if char.isalnum() or char in "-_" else "_" for char in value).strip("_") or "project"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a PKPM calculation runbook.")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--project-path", required=True)
    parser.add_argument("--pkpm-version", default="Unknown")
    parser.add_argument("--structure-type", default="Unknown")
    parser.add_argument("--design-code", default="Confirm with user")
    parser.add_argument("--deliverable", action="append", default=[])
    parser.add_argument("--assumption", action="append", default=[])
    parser.add_argument("--output", required=True, help="Markdown output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    output.write_text(build_runbook(args), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
