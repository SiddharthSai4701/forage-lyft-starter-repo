import unittest
from datetime import datetime
from spindler_battery import SpindlerBattery

class SpindlerTest(unittest.TestCase):
    def does_need_service(self):
        current_date = datetime.today().year
        last_service_date = 2019
        battery = SpindlerBattery(last_service_date, current_date)
        print(battery.needs_service())
        self.assertTrue(battery.needs_service())

    def does_not_need_service(self):
        current_date = datetime.today().year
        last_service_date = 2023
        battery = SpindlerBattery(last_service_date, current_date)
        print(battery.needs_service())
        self.assertFalse(battery.needs_service())

    

test = SpindlerTest()
test.does_not_need_service()