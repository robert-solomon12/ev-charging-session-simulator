"""
visualization.py

Functions for visualizing EV charging session data.
Author: Robert Solomon
"""

import matplotlib.pyplot as plt


def plot_soc_over_time(steps, output_path="data/soc_over_time.png"):
    """
    Plot battery state of charge (SOC) over time.
    """
    times = [step.time_hours for step in steps]
    soc_values = [step.soc for step in steps]

    plt.figure(figsize=(10, 6))
    plt.plot(times, soc_values, marker="o")
    plt.title("EV Charging Session: State of Charge Over Time")
    plt.xlabel("Time (hours)")
    plt.ylabel("State of Charge (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()