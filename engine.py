from abc import ABC, abstractmethod
from car import Car


class Engine(ABC):
    def __init__(self, engine):
        self.engine = engine

    def engine_needs_service(self):
        if self.engine :
            return True
        else:
            return False