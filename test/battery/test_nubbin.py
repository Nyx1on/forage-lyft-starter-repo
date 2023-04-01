import unittest
from datetime import datetime

from battery.nubbinbattery import NubbinBatttery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBatttery(last_service_date)
        self.assertTrue(battery.battery_should_serviced())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = NubbinBatttery(last_service_date)
        self.assertFalse(battery.battery_should_serviced())