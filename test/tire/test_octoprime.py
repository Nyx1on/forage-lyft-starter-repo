import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [1,1,1,0.5]
        tire = OctoprimeTire(wear)
        self.assertTrue(tire.tire_should_serviced())

    def test_needs_service_false(self):
        wear = [0.25,0.25,0.25,1]
        tire = OctoprimeTire(wear)
        self.assertFalse(tire.tire_should_serviced())