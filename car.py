"""
The Car class implements the Serviceable interface to check whether the car requires servicing
It does so by taking the battery and engine and making calls to the respective service methods to check when the service is due
Id either the battery or the engine require servicing, the Car needs to be serviced
"""
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
