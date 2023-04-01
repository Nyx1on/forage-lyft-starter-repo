from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tire):
        self.tire = tire
    
    def tire_needs_service(self):
        if self.tire :
            return True
        else:
            return False