# PKPM calculation workflow reference

## Input information to collect

- Project name, model path, PKPM version, and modules to run.
- Applicable codes/standards and design stage.
- Structural system, story count, typical story height, basement/roof assumptions.
- Materials: concrete grades, reinforcement grades, steel grades, masonry if relevant.
- Loads: dead/live loads, partitions, facade, roof, equipment, wind, seismic, temperature, special loads.
- Seismic parameters: fortification intensity, design earthquake group, site class, characteristic period, damping, importance factor, response spectrum assumptions.
- Output requirements: calculation report, warning list, reinforcement drawings, model archive, review memo.

## Pre-run checks

- Work only on a copied model; preserve the original folder unchanged.
- Confirm axis grid, story definition, standard floors, member sections, constraints, slab openings, transfer stories, basements, and load cases.
- Resolve missing files, database repair prompts, abnormal story definitions, and material/library prompts before calculation.
- Record all user-confirmed assumptions that are not visible in the model.

## Suggested module sequence

1. Open copied project and verify PMCAD/model data.
2. Run model integrity or preprocessing checks if available.
3. Generate analysis data for SATWE or the target structural analysis module.
4. Run structural analysis and design.
5. Review warnings/errors and rerun only after documenting the correction.
6. Export result tables, calculation book, and drawings/reinforcement outputs requested by the user.

## Result review categories

- Fatal errors and warnings from preprocessing or analysis.
- Global indicators: periods, period ratio, mass participation, base shear, shear-weight ratio, displacement/drift, torsional irregularity.
- Story indicators: stiffness ratio, shear distribution, weak story, soft story, mass/stiffness irregularity.
- Member indicators: axial compression ratio, shear capacity, reinforcement limits, section overstress, beam-column joint issues.
- Foundation or basement interactions if included in the selected module.
- Drawing/report completeness and consistency with the final calculated model.

## Escalation triggers

Pause and ask the user or responsible engineer when any of these occur:

- PKPM asks to repair, upgrade, synchronize, overwrite, or rebuild model data.
- A calculation fails, hangs, or returns fatal errors.
- A parameter value is unknown or conflicts with project documentation.
- The model shows major irregularities, over-limit warnings, or repeated non-convergence.
- Any action could overwrite original files or final deliverables.
