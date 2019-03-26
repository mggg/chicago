# MGGG Chicago Report

## Contents

- `ensembles/`
  - Jupyter notebooks with our code for the MCMC runs generated using [gerrychain](https://github.com/mggg/gerrychain). See also [hangulu/mggg_chicago](https://github.com/hangulu/mggg_chicago) for Jupyter notebooks that the notebooks included here are based on.
  - Tabular results in from our MCMC runs, with the ward-level demographics of each districting plan in each of the ensembles.
  - `districtr_plans.zip`: Complete ensembles (50x1, 10x5, and 10x5 CA) in a format that can be imported into [Districtr](https://mggg.org/Districtr/new).
- `projection/`: Code and results of our demographic threshold model projections, as described in section 5 of the report.
- `ranked_choice/`:
  - Ranked-choice ballot data from Cambridge, Minneapolis, and Oakland.
  - Partial candidate demographic identifications
  - Cleaning scripts for the preference schedules
  - Code for running hypothetical single transferable vote elections using the real preference schedule data. This code uses the [rcv](https://github.com/gerrymandr/rcv) package, which was created by MGGG during this project.
- `shapefiles/`: Cleaned shapefiles with demographics and election data joined. See also [mggg-states/IL-shapefiles](https://github.com/mggg-states/IL-shapefiles).
