"""
I want to make different types of objects that need to satisfy some basic
protocol class so that they can be used similarly by the client code
despite exhibiting nuanced implementation differences.
"""
from dataclasses import dataclass
from typing import Protocol, List
from robots.status import Status

@dataclass
class Sensor:
    id: str
    type: str
    reading_value: float
    reading_units: str
    accuracy: float

class Robot(Protocol):
    def turn_on(self) -> Status:
        """
        Powering on the robot may cause something to break,
        so a Status value is returned for monitoring system health.
        """
        ...
    def turn_off(self) -> Status:
        """
        Powering off the robot may cause something to break
        if it was in the middle of doing something,
        so a Status value is returned for monitoring system health.
        """
        ...
    def is_on(self) -> bool:
        """
        Just checks whether-or-not the robot is powered-on,
        this action cannot cause something to break, so Just
        return a boolean value.
        """
        ...
    def read_all_sensors(self) -> List(Sensor):
        """
        Returns a list of sensor objects whose values can be interrogated.
        """
        ...
