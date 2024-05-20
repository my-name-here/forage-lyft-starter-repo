import unittest
from datetime import datetime

import engine


class TestEngines(unittest.TestCase):

    def test_CapuletEngine_needsService(self):
        lastServiceMilage = 0
        currentMilage = 31000
        Newengine = engine.CapuletEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())

    def test_CapuletEngineDoesNotNeedService(self):
        lastServiceMilage = 0
        currentMilage = 29000
        Newengine = engine.CapuletEngine(lastServiceMilage, currentMilage)
        self.assertTrue(Newengine.needs_service())



if __name__ == '__main__':
    unittest.main()
