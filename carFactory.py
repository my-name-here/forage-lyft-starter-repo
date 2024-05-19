
from car import Car
from engine import *
from battery import *
class carFactory:
    def __init__(self):
        self.engine = None
        self.battery = None
        self.car = None
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.car = Car(self.engine, self.battery)
    