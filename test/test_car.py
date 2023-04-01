import unittest
from datetime import datetime

from abc import ABC, abstractmethod

from carfactory import CarFactory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_calliope(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        
        self.assertTrue(test_battery)

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_calliope(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        self.assertFalse(test_battery)

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory().create_calliope(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()
        
        self.assertTrue(test_engine)

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory().create_calliope(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()

        self.assertFalse(test_engine)


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_glissade(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        
        self.assertTrue(test_battery)

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_glissade(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        self.assertFalse(test_battery)

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory().create_glissade(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()
        
        self.assertTrue(test_engine)

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory().create_glissade(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()
        
        self.assertFalse(test_engine)


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = CarFactory().create_palindrome(last_service_date, warning_light_is_on)
        test_battery = car.needs_service()
        
        self.assertTrue(test_battery)

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = CarFactory().create_palindrome(last_service_date, warning_light_is_on)
        test_battery = car.needs_service()
        
        self.assertFalse(test_battery)

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory().create_palindrome(last_service_date, warning_light_is_on)
        test_engine = car.needs_service()
        
        self.assertTrue(test_engine)

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory().create_palindrome(last_service_date, warning_light_is_on)
        test_engine = car.needs_service()
        
        self.assertFalse(test_engine)


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        
        self.assertTrue(test_battery)

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        self.assertFalse(test_battery)

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()
        
        self.assertTrue(test_engine)

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()
        
        self.assertFalse(test_engine)


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_throvex(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        self.assertTrue(test_battery)

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_throvex(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        
        self.assertFalse(test_battery)

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory().create_throvex(last_service_date, current_mileage, last_service_mileage)
        test_battery = car.needs_service()
        
        self.assertTrue(test_battery)

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory().create_throvex(last_service_date, current_mileage, last_service_mileage)
        test_engine = car.needs_service()
        self.assertFalse(test_engine)


if __name__ == '__main__':
    unittest.main()
