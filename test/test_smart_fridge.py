import unittest
import SmartFridge.SmartFridge

class SmartFridgeShould(unittest.TestCase):
    def test_unittest(self):
        assert(True)

    def test_smart_fridge(self):
        assert(SmartFridge.test())

if __name__ == '__main__':
    unittest.main()