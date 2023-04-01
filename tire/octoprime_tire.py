from datetime import datetime

from tire.tire import Tire

class OctoprimeTire():
    def __init__(self, wear):
        self.wear = wear
    
    def tire_should_serviced(self):
        sum = 0
        for wear_num in self.wear:
            sum = sum + wear_num
        
        if sum >= 3 :
            return True
        else:
            return False