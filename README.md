# ECE 105 — Sensor Plot Generation

## Overview

This repository contains a small utility to generate synthetic temperature sensor data and produce publication-quality plots (scatter, histogram, boxplot) as PNG files. The data and plotting code were adapted from a Jupyter notebook (lab3_sensor_plots.ipynb) and are exposed in a standalone script `generate_plots.py`.

## Installation

1. Activate the course environment:

```bash
conda activate ece105
```

2. Install dependencies (choose one):

```bash
conda install -c conda-forge numpy matplotlib
# or with mamba
mamba install -c conda-forge numpy matplotlib
```

## Usage

Run the script from the repository root:

```bash
python generate_plots.py
```

The script's `main()` uses a default RNG seed (4309). You can call the script programmatically or modify `main()` arguments (seed, outdir, show) if you import functions from `generate_plots.py`.

## Output

Running the script produces three PNG files (saved in the current working directory by default):

- `scatter.png` — scatter plot of temperature (y) vs time (x) for Sensor A and Sensor B
- `histogram.png` — overlaid histogram comparing Sensor A and Sensor B distributions
- `boxplot.png` — side-by-side box plots with an overall mean line

Each plot is saved at 300 DPI and formatted for readability.

## AI tools used and disclosure

Placeholder: describe here any AI assistance used to generate code, documentation, or other artifacts (models, prompts, and review/verification steps).

## License

Add license text here if needed.
