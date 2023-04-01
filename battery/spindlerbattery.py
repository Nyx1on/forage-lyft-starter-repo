from datetime import datetime

from battery.battery import Battery

class SpindlerBatttery():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.today().date()
    
    def battery_should_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < self.current_date :
            return True
        else:
            return False