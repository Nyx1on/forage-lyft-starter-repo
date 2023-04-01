from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        if self.engine or self.battery or self.tire:
            return True
        else:
            return False

   

