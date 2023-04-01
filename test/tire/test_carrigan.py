import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [1,0,0.5,0.25]
        tire = CarriganTire(wear)
        self.assertTrue(tire.tire_should_serviced())

    def test_needs_service_false(self):
        wear = [0.5,0.25,0.35,0.90]
        tire = CarriganTire(wear)
        self.assertFalse(tire.tire_should_serviced())