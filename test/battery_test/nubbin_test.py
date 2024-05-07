import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery

class NubbinTest:
    def does_need_service(self):
        current_date = datetime.today().year
        last_service_date = '2019-03-12'
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

