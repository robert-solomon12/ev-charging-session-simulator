"""
charger.py

Defines the Charger class.
Author: Robert Solomon
"""


class Charger:
    def __init__(self, charger_name: str, power_kw: float, price_per_kwh: float):
        self.charger_name = charger_name
        self.power_kw = power_kw
        self.price_per_kwh = price_per_kwh