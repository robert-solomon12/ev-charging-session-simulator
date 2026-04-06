"""
vehicle.py

Defines the ElectricVehicle class and predefined EV profiles.
Author: Robert Solomon
"""

from dataclasses import dataclass


@dataclass
class ElectricVehicle:
    """
    Represents an electric vehicle with a battery and current charge level.
    """
    model_name: str
    battery_capacity_kwh: float
    current_soc: float

    def energy_needed_to_target(self, target_soc: float) -> float:
        """
        Calculate how much energy (kWh) is needed to charge
        from the current state of charge to the target state of charge.
        """
        if target_soc <= self.current_soc:
            return 0.0

        soc_difference = target_soc - self.current_soc
        return (soc_difference / 100) * self.battery_capacity_kwh


# Predefined EV profiles
EV_PROFILES = {
    "tesla_model_3": {
        "model_name": "Tesla Model 3",
        "battery_capacity_kwh": 60.0,
    },
    "nissan_leaf": {
        "model_name": "Nissan Leaf",
        "battery_capacity_kwh": 40.0,
    },
    "bmw_i4": {
        "model_name": "BMW i4",
        "battery_capacity_kwh": 83.9,
    },
}


def create_vehicle_from_profile(profile_key: str, current_soc: float) -> ElectricVehicle:
    """
    Create an ElectricVehicle instance from a predefined profile.
    """
    if profile_key not in EV_PROFILES:
        available_profiles = ", ".join(EV_PROFILES.keys())
        raise ValueError(
            f"Unknown profile '{profile_key}'. Available profiles: {available_profiles}"
        )

    profile = EV_PROFILES[profile_key]

    return ElectricVehicle(
        model_name=profile["model_name"],
        battery_capacity_kwh=profile["battery_capacity_kwh"],
        current_soc=current_soc,
    )