"""
main.py

Entry point for the EV Charging Session Simulator.
Author: Robert Solomon
"""

from vehicle import ElectricVehicle
from charger import Charger
from session import ChargingSession
from utils import save_session_to_csv


def main():
    print("=== EV Charging Session Simulator ===")

    vehicle = ElectricVehicle(
        model_name="Tesla Model 3",
        battery_capacity_kwh=60.0,
        current_soc=25.0
    )

    charger = Charger(
        charger_name="DC Fast Charger",
        power_kw=50.0,
        price_per_kwh=0.35
    )

    target_soc = 80.0

    session = ChargingSession(vehicle, charger, target_soc)
    result = session.run()

    print("\n--- Charging Summary ---")
    print(f"Vehicle: {vehicle.model_name}")
    print(f"Current SOC: {vehicle.current_soc}%")
    print(f"Target SOC: {target_soc}%")
    print(f"Charger: {charger.charger_name} ({charger.power_kw} kW)")
    print(f"Energy Added: {result.energy_added_kwh} kWh")
    print(f"Time Needed: {result.charging_time_hours} hours")
    print(f"Estimated Cost: €{result.charging_cost}")
    print(f"Final SOC: {result.final_soc}%")

    save_session_to_csv("data/charging_sessions.csv", vehicle.model_name, charger.charger_name, result)
    print("\nSession saved to data/charging_sessions.csv")


if __name__ == "__main__":
    main()