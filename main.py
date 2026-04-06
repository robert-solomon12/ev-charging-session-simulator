"""
main.py

Entry point for the EV Charging Session Simulator.
Author: Robert Solomon
"""

from vehicle import EV_PROFILES, create_vehicle_from_profile
from charger import Charger
from session import ChargingSession
from utils import save_session_to_csv


def main():
    print("=== EV Charging Session Simulator ===")

    # Choose a predefined EV profile
    selected_profile = "bmw_i4"
    current_soc = 25.0
    target_soc = 80.0

    vehicle = create_vehicle_from_profile(
        profile_key=selected_profile,
        current_soc=current_soc
    )

    charger = Charger(
        charger_name="DC Fast Charger",
        power_kw=50.0,
        price_per_kwh=0.35
    )

    session = ChargingSession(vehicle, charger, target_soc)
    result = session.run()

    print("\n--- Available EV Profiles ---")
    for key, profile in EV_PROFILES.items():
        print(f"- {key}: {profile['model_name']} ({profile['battery_capacity_kwh']} kWh)")

    print("\n--- Charging Summary ---")
    print(f"Selected Profile: {selected_profile}")
    print(f"Vehicle: {vehicle.model_name}")
    print(f"Battery Capacity: {vehicle.battery_capacity_kwh} kWh")
    print(f"Current SOC: {vehicle.current_soc}%")
    print(f"Target SOC: {target_soc}%")
    print(f"Charger: {charger.charger_name} ({charger.power_kw} kW)")
    print(f"Energy Added: {result.energy_added_kwh} kWh")
    print(f"Time Needed: {result.charging_time_hours} hours")
    print(f"Estimated Cost: €{result.charging_cost}")
    print(f"Final SOC: {result.final_soc}%")

    save_session_to_csv(
        "data/charging_sessions.csv",
        vehicle.model_name,
        charger.charger_name,
        result
    )
    print("\nSession saved to data/charging_sessions.csv")


if __name__ == "__main__":
    main()