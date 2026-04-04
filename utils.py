"""
utils.py

Utility functions for saving charging session results.
"""

import csv
from datetime import datetime
from pathlib import Path


def save_session_to_csv(filename: str, vehicle_name: str, charger_name: str, result):
    """
    Save a charging session result to a CSV file.
    """
    file_path = Path(filename)
    file_exists = file_path.exists()

    with open(file_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "vehicle",
                "charger",
                "energy_added_kwh",
                "charging_time_hours",
                "charging_cost",
                "final_soc"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            vehicle_name,
            charger_name,
            result.energy_added_kwh,
            result.charging_time_hours,
            result.charging_cost,
            result.final_soc
        ])