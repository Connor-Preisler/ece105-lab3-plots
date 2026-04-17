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
# Create plot_histogram(sensor_a, sensor_b, timestamps, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_histogram(ax, sensor_a, sensor_b, bins=30, alpha=0.5, title='Overlaid histogram of Sensor A and Sensor B'):
    """
    Overlaid histogram comparing two sensor temperature distributions.
 
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to draw on (modified in place).
    sensor_a : array_like, shape (N,)
        Sensor A temperature readings (°C).
    sensor_b : array_like, shape (N,)
        Sensor B temperature readings (°C).
    bins : int, optional
        Number of histogram bins (default 30).
    alpha : float, optional
        Transparency for histogram bars (default 0.5).
    title : str, optional
        Plot title (default provided).
 
    Returns
    -------
    None
        Draws on `ax` in place and returns None.
 
    Notes
    -----
    Uses shared bin edges so the two histograms are directly comparable.
    Draws vertical dashed lines at each sensor's mean and includes a legend.
    """
    import numpy as np
 
    sa = np.asarray(sensor_a, dtype=np.float64)
    sb = np.asarray(sensor_b, dtype=np.float64)
 
    if sa.ndim != 1 or sb.ndim != 1:
        raise ValueError("sensor_a and sensor_b must be 1-D arrays")
    if sa.shape[0] != sb.shape[0]:
        # Histograms may be plotted with unequal lengths, but warn/handle gracefully:
        # proceed without enforcing equal length; remove this check if unequal lengths are allowed.
        pass
 
    # shared bin edges: bins -> number of intervals
    edges = np.linspace(min(sa.min(), sb.min()), max(sa.max(), sb.max()), bins + 1)
 
    color_a = 'blue'
    color_b = 'orange'
 
    ax.hist(sa, bins=edges, color=color_a, alpha=alpha, edgecolor='k', label='Sensor A')
    ax.hist(sb, bins=edges, color=color_b, alpha=alpha, edgecolor='k', label='Sensor B')
 
    # vertical dashed lines at means
    ax.axvline(sa.mean(), color=color_a, linestyle='--', linewidth=1.5, label=f'Sensor A mean = {sa.mean():.2f} °C')
    ax.axvline(sb.mean(), color=color_b, linestyle='--', linewidth=1.5, label=f'Sensor B mean = {sb.mean():.2f} °C')
 
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title(title)
    ax.legend(loc='best')
 
    return None
# Create box_plot(sensor_a, sensor_b, timestamps, ax) that draws
# the box_plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_boxplot(ax, sensor_a, sensor_b, labels=('Sensor A', 'Sensor B'), title='Side-by-side box plot: Sensor A vs Sensor B'):
    """
    Side-by-side box plot comparing two sensor temperature distributions.
 
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to draw on (modified in place).
    sensor_a : array_like, shape (N,)
        Sensor A temperature readings (°C).
    sensor_b : array_like, shape (M,)
        Sensor B temperature readings (°C).
    labels : tuple of str, optional
        Labels for the two boxes (default ('Sensor A', 'Sensor B')).
    title : str, optional
        Plot title.
 
    Returns
    -------
    None
        Draws on `ax` in place and returns None.
 
    Notes
    -----
    Draws boxplots side-by-side, colors the boxes, and adds a horizontal dashed
     line at the overall mean of both sensors combined.
    """
    import numpy as np
    from matplotlib.patches import Patch
 
    sa = np.asarray(sensor_a, dtype=np.float64)
    sb = np.asarray(sensor_b, dtype=np.float64)
 
    if sa.ndim != 1 or sb.ndim != 1:
        raise ValueError("sensor_a and sensor_b must be 1-D arrays")
 
    # overall mean across both sensors
    overall_mean = np.mean(np.concatenate([sa, sb]))
 
    # Create boxplot (patch_artist=True so boxes can be colored)
    bp = ax.boxplot([sa, sb], labels=list(labels), patch_artist=True)
 
    # Color the boxes
    colors = ['C0', 'C1']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('k')
 
    # Style medians
    for median in bp.get('medians', []):
        median.set(color='black', linewidth=1.2)
 
    # Axis labels / title
    ax.set_xlabel('')
    ax.set_xticks([1, 2])
    ax.set_xticklabels(labels)
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title(title)
 
    # Horizontal dashed line at overall mean
    mean_line = ax.axhline(overall_mean, color='k', linestyle='--', linewidth=1.0)
 
    # Make a legend: colored patches for the sensors + the mean line
    handles = [Patch(facecolor=colors[0], edgecolor='k', label=labels[0]),
                Patch(facecolor=colors[1], edgecolor='k', label=labels[1]),mean_line]
    labels_legend = [labels[0], labels[1], f'Overall mean = {overall_mean:.2f} °C']
    ax.legend(handles=handles, labels=labels_legend, loc='best')
 
    return None
# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.
def main(seed=4309, outdir='.', show=False):
    """
    Generate data and save scatter, histogram, and boxplot PNGs.
 
    Parameters
    ----------
    seed : int, optional
        RNG seed passed to generate_data (default 4309).
    outdir : str, optional
        Directory where PNG files will be saved (default current directory).
    show : bool, optional
        If True, display each figure interactively with plt.show() (default False).
 
    Returns
    -------
    None
        Files written: scatter.png, histogram.png, boxplot.png in `outdir`.
    """
    import os
    import matplotlib.pyplot as plt
 
    os.makedirs(outdir, exist_ok=True)
 
    # Generate data
    timestamps, sensor_a, sensor_b = generate_data(seed)
 
    # Scatter plot
    fig, ax = plt.subplots(figsize=(8, 4))
    plot_scatter(ax, timestamps, sensor_a, sensor_b, title='Sensor readings vs Time')
    fig.savefig(os.path.join(outdir, 'scatter.png'), dpi=300)
    if show:
        plt.show()
    plt.close(fig)
 
    # Histogram
    fig, ax = plt.subplots(figsize=(8, 4))
    plot_histogram(ax, sensor_a, sensor_b, bins=30, alpha=0.5,title='Overlaid histogram of Sensor A and Sensor B')
    fig.savefig(os.path.join(outdir, 'histogram.png'), dpi=300)
    if show:
        plt.show()
    plt.close(fig)
 
    # Boxplot
    fig, ax = plt.subplots(figsize=(6, 4))
    plot_boxplot(ax, sensor_a, sensor_b,
                labels=('Sensor A', 'Sensor B'),
                title='Side-by-side box plot: Sensor A vs Sensor B')
    fig.savefig(os.path.join(outdir, 'boxplot.png'), dpi=300)
    if show:
        plt.show()
    plt.close(fig)
 
    return None
 
 
if __name__ == '__main__':
     main()