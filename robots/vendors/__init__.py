"""
A collection of different types of approved vendors.
"""
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Product:
    name: str
    type: str
    price: float
    url: str

@dataclass(frozen=True)
class Vendor:
    name: str
    products: List[Product]
    location: str
    url: str
