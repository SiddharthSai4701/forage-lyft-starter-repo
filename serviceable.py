"""
The serviceable interface contains an abstract method which can be implemented by both batteries and engines based on their servicing requirements.
It can also be implemented by other parts of the vehicle that may require replacement, like the tyres.
"""
from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass