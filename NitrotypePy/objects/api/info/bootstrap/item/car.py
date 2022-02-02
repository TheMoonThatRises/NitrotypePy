from typing import List
from .basic_object import Options


class Car:
    def __init__(self):
        self.id: int
        self.carID: int
        self.name: str
        self.longDescription: str
        self.options: Options
        self.enterSound: str
        self.price: int
        self.lastModified: int
