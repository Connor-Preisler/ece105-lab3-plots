"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np
   
def generate_data(seed):
    """
    Generate synthetic temperature sensor data for two sensors.
   
    Parameters
    ----------
    seed : int
         Seed for the NumPy random generator (passed to np.random.default_rng).
   
    Returns
    -------
    timestamps : ndarray, shape (200,), dtype float64
        Evenly spaced timestamps from 0.0 to 10.0 seconds.
    sensor_a : ndarray, shape (200,), dtype float64
        Sensor A temperature readings (Gaussian, loc=25.0 °C, scale=3.0 °C).
    sensor_b : ndarray, shape (200,), dtype float64
           Sensor B temperature readings (Gaussian, loc=27.0 °C, scale=4.5 °C).
   
    Notes
    -----
    Uses np.random.default_rng for reproducible, modern RNG behavior.
    """
    rng = np.random.default_rng(seed)
    n = 200
    timestamps = np.linspace(0.0, 10.0, n, dtype=np.float64)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n).astype(np.float64)
    return timestamps, sensor_a, sensor_b
