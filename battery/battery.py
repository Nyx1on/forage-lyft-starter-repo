from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, battery):
        self.battery = battery
    
    def battery_needs_service(self):
        if self.battery :
            return True
        else:
            return False