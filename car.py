from abc import ABC, abstractmethod
from Servicable import Servicable

class Car(Servicable, ABC):
    def __init__(self, engine, battery, wearArray):
        super().__init__()
        self.battery = battery
        self.engine = engine
        self.wearArray = wearArray

    @abstractmethod
    def needs_service(self):
        return (self.engine.needs_service() or self.battery.needs_service())
