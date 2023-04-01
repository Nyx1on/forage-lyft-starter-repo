from abc import ABC, abstractmethod
from car import Car
from engine import Engine
from battery import Battery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindlerbattery import SpindlerBatttery
from battery.nubbinbattery import NubbinBatttery

class CarFactory(ABC):
    def __init__(self,car_name):
        self.car_name = car_name
    
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        engine = CapuletEngine(current_mileage, last_service_mileage)
        capulet = Engine(engine.engine_should_be_serviced())
        battery = SpindlerBatttery(last_service_date)
        spindler = Battery(battery.battery_should_serviced())

        calliope = Car(capulet,spindler)

        return calliope

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        willoughby = Engine(engine.engine_should_be_serviced())
        battery = SpindlerBatttery(last_service_date)
        spindler = Battery(battery.battery_should_serviced())

        glissade = Car(willoughby,spindler)

        return glissade
    
    def create_palindrome(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

        
        engine = SternmanEngine(warning_light_is_on)
        sternman = Engine(engine.engine_should_be_serviced())
        battery = SpindlerBatttery(last_service_date)
        spindler = Battery(battery.battery_should_serviced())

        palindrome = Car(sternman,spindler)

        return palindrome

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        willoughby = Engine(engine.engine_should_be_serviced())
        battery = NubbinBatttery(last_service_date)
        nubbin = Battery(battery.battery_should_serviced())

        rorschach = Car(willoughby,nubbin)

        return rorschach
    
    def create_throvex(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        engine = CapuletEngine(current_mileage, last_service_mileage)
        capulet = Engine(engine.engine_should_be_serviced())
        battery = NubbinBatttery(last_service_date)
        nubbin = Battery(battery.battery_should_serviced())

        throvex = Car(capulet,nubbin)

        return throvex