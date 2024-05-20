from abc import ABC, abstractmethod
from Servicable import Servicable
import tires
class Car(Servicable, ABC):
    def __init__(self, engine, battery, wearArray, tireType):
        super().__init__()
        self.battery = battery
        self.engine = engine
        self.wearArray = wearArray
        if tireType == "Carrigan":
            self.tire = tires.CarriganTires(wearArray)
        elif tireType == "Octoprime":
            self.tire = tires.OctoprimeTires(wearArray)
        else:
            self.tire = tires.Tires(wearArray)


    @abstractmethod
    def needs_service(self):
        return (self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service())
