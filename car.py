from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def car_needs_service(self):
        if self.engine or self.battery:
            return True
        else:
            return False

    @abstractmethod
    def needs_service(self):
        pass

