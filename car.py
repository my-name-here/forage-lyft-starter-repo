from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        return (self.engine.needs_service() or self.battery.needs_service())
