from abc import ABC, abstractmethod
from car import Car
from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindlerbattery import SpindlerBatttery
from battery.nubbinbattery import NubbinBatttery
from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class CarFactory(ABC):
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage, wear):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.wear = wear

        capulet = CapuletEngine(self.current_mileage, self.last_service_mileage).engine_should_be_serviced()
        engine = Engine(capulet).engine_needs_service()

        spindler = SpindlerBatttery(self.last_service_date).battery_should_serviced()
        battery = Battery(spindler)

        octoprime = OctoprimeTire(self.wear).tire_should_serviced()
        tire = Tire(octoprime)

        calliope = Car(engine,battery,tire)

        return calliope

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage, wear):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.wear = wear

        
        willoughby = WilloughbyEngine(self.current_mileage, self.last_service_mileage).engine_should_be_serviced()
        engine = Engine(willoughby).engine_needs_service()

        spindler = SpindlerBatttery(self.last_service_date).battery_should_serviced()
        battery = Battery(spindler).battery_needs_service()

        octoprime = OctoprimeTire(self.wear).tire_should_serviced()
        tire = Tire(octoprime)

        glissade = Car(engine,battery,tire)

        return glissade
    
    def create_palindrome(self, last_service_date, warning_light_is_on,wear):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on
        self.wear = wear

        
        sternman = SternmanEngine(self.warning_light_is_on).engine_should_be_serviced()
        engine = Engine(sternman).engine_needs_service()

        spindler = SpindlerBatttery(self.last_service_date).battery_should_serviced()
        battery = Battery(spindler).battery_needs_service()

        carrigan = CarriganTire(self.wear).tire_should_serviced()
        tire = Tire(carrigan)

        palindrome = Car(engine,battery,tire)

        return palindrome

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage, wear):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.wear = wear

        
        willoughby = WilloughbyEngine(self.current_mileage, self.last_service_mileage).engine_should_be_serviced()
        engine = Engine(willoughby).engine_needs_service()

        nubbin = NubbinBatttery(self.last_service_date).battery_should_serviced()
        battery = Battery(nubbin).battery_needs_service()

        carrigan = CarriganTire(self.wear).tire_should_serviced()
        tire = Tire(carrigan)

        rorschach = Car(engine,battery,tire)

        return rorschach
    
    def create_throvex(self, last_service_date, current_mileage, last_service_mileage, wear):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.wear = wear

        capulet = CapuletEngine(self.current_mileage, self.last_service_mileage).engine_should_be_serviced()
        engine = Engine(capulet).engine_needs_service()

        nubbin = NubbinBatttery(self.last_service_date).battery_should_serviced()
        battery = Battery(nubbin).battery_needs_service()

        carrigan = CarriganTire(self.wear).tire_should_serviced()
        tire = Tire(carrigan)

        throvex = Car(engine,battery,tire)

        return throvex