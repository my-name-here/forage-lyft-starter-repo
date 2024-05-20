from abc import ABC, abstractmethod

class Tires(ABC):
    def __init__(self, wearArray):
        self.wearArray = wearArray

    @abstractmethod
    def needs_service(self):
        return True

class CarriganTires(Tires):
    def __init__(self, wearArray):
        super.__init__(self, wearArray)
    def needs_service(self):
        TireNeedsService = [tireWear>=0.9 for tireWear in self.wearArray]
        return True in TireNeedsService


class OctoprimeTires(Tires):
    def __init__(self, wearArray):
        super.__init__(self, wearArray)
    def needs_service(self):

        return sum(self.wearArray)>=3
