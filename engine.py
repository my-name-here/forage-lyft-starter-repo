from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def needs_service(self):
        return True


class CapuletEngine(Engine):
    def __init__(self, lastServiceMilage, currentMilage):
        Engine.__init__(self)
        self.lastServiceMilage = lastServiceMilage
        self.currentMilage = currentMilage

    def needs_service(self):
        return (self.currentMilage - self.lastServiceMilage)>30000

class WilloughbyEngine(Engine):
    def __init__(self, lastServiceMilage, currentMilage):
        Engine.__init__(self)
        self.lastServiceMilage = lastServiceMilage
        self.currentMilage = currentMilage

    def needs_service(self):
        return (self.currentMilage - self.lastServiceMilage)>60000


class SternmanEngine(Engine):
    def __init__(self, warningLightOn):
        Engine.__init__(self)
        self.warningLightOn = warningLightOn

    def needs_service(self):
        return self.warningLightOn