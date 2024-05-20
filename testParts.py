import unittest
from datetime import datetime

import engine
import battery


class TestEngines(unittest.TestCase):

    def test_CapuletEngine_needsService(self):
        lastServiceMilage = 0
        currentMilage = 30001
        Newengine = engine.CapuletEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())

    def test_CapuletEngine_DoesNotNeedService(self):
        lastServiceMilage = 0
        currentMilage = 30000
        Newengine = engine.CapuletEngine(lastServiceMilage, currentMilage)
        self.assertFalse(Newengine.needs_service())

    def test_WilloughbyEngine_needsService(self):
        lastServiceMilage = 0
        currentMilage = 60001
        Newengine = engine.WilloughbyEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())

    def test_WilloughbyEngine_DoesNotNeedService(self):
        lastServiceMilage = 0
        currentMilage = 60000
        Newengine = engine.WilloughbyEngine(lastServiceMilage, currentMilage)
        self.assertFalse(Newengine.needs_service())

    def test_SternmanEngine_needsService(self):
        warningLightOn = True
        Newengine = engine.SternmanEngine(warningLightOn)
        self.assertTrue(Newengine.needs_service())

    def test_SternmanEngine_DoesNotNeedService(self):
        warningLightOn = False

        Newengine = engine.SternmanEngine(warningLightOn)
        self.assertFalse(Newengine.needs_service())

class TestBattery(unittest.TestCase):

    def test_SpindlerBattery_needsService(self):
        currentDate = datetime.today().date()
        lastServiced = currentDate.replace(year= currentDate.year - 2)
        NewBattery = battery.SpindlerBattery(lastServiced, currentDate)
        self.assertTrue(NewBattery.needs_service())

    def test_SpindlerBattery_DoesNotNeedService(self):
        currentDate = datetime.today().date()
        lastServiced = currentDate.replace(year= currentDate.year - 1)
        NewBattery = battery.SpindlerBattery(lastServiced, currentDate)
        self.assertFalse(NewBattery.needs_service())

    def test_NubbinBattery_needsService(self):
        currentDate = datetime.today().date()
        lastServiced = currentDate.replace(year= currentDate.year - 4)
        NewBattery = battery.NubbinBattery(lastServiced, currentDate)
        self.assertTrue(NewBattery.needs_service())

    def test_NubbinBattery_DoesNotNeedService(self):
        currentDate = datetime.today().date()
        lastServiced = currentDate.replace(year= currentDate.year - 3)
        NewBattery = battery.NubbinBattery(lastServiced, currentDate)
        self.assertFalse(NewBattery.needs_service())


if __name__ == '__main__':
    unittest.main()
