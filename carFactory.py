
from car import Car
from engine import *
from battery import *
class CarFactory:
    def __init__(self):
        self.engine = None
        self.battery = None
        self.car = None
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.car = Car(self.engine, self.battery)
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.car = Car(self.engine, self.battery)
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.engine = SternmanEngine(warning_light_on)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.car = Car(self.engine, self.battery)
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.car = Car(self.engine, self.battery)
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.car = Car(self.engine, self.battery)