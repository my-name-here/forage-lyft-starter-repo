import unittest
from datetime import datetime

import engine


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
        self.assertTrue(Newengine.needs_service())

    def test_WilloughbyEngine_needsService(self):
        lastServiceMilage = 0
        currentMilage = 60001
        Newengine = engine.WilloughbyEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())

    def test_WilloughbyEngine_DoesNotNeedService(self):
        lastServiceMilage = 0
        currentMilage = 60000
        Newengine = engine.WilloughbyEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())

    def test_SternmanEngine_needsService(self):
        warningLightOn = True
        Newengine = engine.SternmanEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())

    def test_SternmanEngine_DoesNotNeedService(self):
        warningLightOn = False

        Newengine = engine.SternmanEngine(warningLightOn)
        self.assertTrue(Newengine.needs_service())



if __name__ == '__main__':
    unittest.main()
