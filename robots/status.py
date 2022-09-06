"""
A collection of different Statuses.
"""
from dataclasses import dataclass

@dataclass
class Status:
    name: str
    id: int
    description: str
