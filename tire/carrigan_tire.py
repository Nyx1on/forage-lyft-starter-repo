from datetime import datetime

from tire.tire import Tire

class CarriganTire():
    def __init__(self, wear):
        self.wear = wear
   
    def tire_should_serviced(self):
        for wear_num in self.wear:
            if wear_num > 0.9 :
                return True
            else:
                return False
