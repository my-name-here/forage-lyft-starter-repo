from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def needs_service(self):
        return True


class SpindlerBattery(Battery):
    def __init__(self, lastServiceDate, currentDate):
        Battery.__init__(self)
        self.lastServiceDate = lastServiceDate
        self.currentDate = currentDate

    def needs_service(self):
        return (self.currentDate.year - self.lastServiceDate.year)>=2


class NubbinBattery(Battery):
    def __init__(self, lastServiceDate, currentDate):
        Battery.__init__(self)
        self.lastServiceDate = lastServiceDate
        self.currentDate = currentDate

    def needs_service(self):
        return (self.currentDate.year - self.lastServiceDate.year)>=4