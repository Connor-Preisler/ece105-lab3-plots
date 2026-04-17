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
# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(ax, timestamps, sensor_a, sensor_b, title='Sensor readings vs Time'):
    """
     Scatter plot of two temperature sensors vs time onan existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to draw on (modified in place).
    timestamps : ndarray, shape (N,)
        Time values in seconds (x-axis).
    sensor_a : ndarray, shape (N,)
        Sensor A temperature readings (°C).
    sensor_b : ndarray, shape (N,)
        Sensor B temperature readings (°C).
    title : str, optional
        Plot title (default 'Sensor readings vs Time').

    Returns
    -------
    None
        The function draws on ax and returns None.
    """
    import numpy as np

    t = np.asarray(timestamps)
    sa = np.asarray(sensor_a)
    sb = np.asarray(sensor_b)

    if t.ndim != 1 or sa.ndim != 1 or sb.ndim != 1:
        raise ValueError("timestamps, sensor_a, sensor_b must be 1-D arrays")
    if not (t.shape[0] == sa.shape[0] == sb.shape[0]):
        raise ValueError("timestamps, sensor_a, sensor_b must have the same length")

    ax.scatter(t, sa, color='blue', edgecolors='k', s=40, alpha=0.9, label='Sensor A')
    ax.scatter(t, sb, color='orange', edgecolors='k', s=40, alpha=0.9, label='Sensor B')

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title(title)
    ax.legend(loc='best')
    ax.grid(alpha=0.25)

    return None