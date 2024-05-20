from abc import ABC, abstractmethod
from Servicable import Servicable
import tires
class Car(Servicable, ABC):
    def __init__(self, engine, battery, wearArray, tireType):
        super().__init__()
        self.battery = battery
        self.engine = engine
        self.wearArray = wearArray
        self.tire = tires.CarriganTires(wearArray) if tireType == "Carrigan" else tires.OctoprimeTires(wearArray)

    @abstractmethod
    def needs_service(self):
        return (self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service())
