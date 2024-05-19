from abc import ABC, abstractmethod
from engine import Engine

class CapuletEngine(Engine,ABC):
    def __init__(self, lastServiceMilage, currentMilage):
        self.lastServiceMilage = lastServiceMilage
        self.currentMilage = currentMilage

    def needs_service(self):
        return (self.currentMilage - self.lastServiceMilage)>30000
