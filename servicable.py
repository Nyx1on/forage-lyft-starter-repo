from abc import ABC, abstractmethod
from car import Car

class Servicable(Car):
        def __init__(self, car):
            self.car = car

        def needs_service(self):
             if self.car :
                   return True
             else:
                   return False
