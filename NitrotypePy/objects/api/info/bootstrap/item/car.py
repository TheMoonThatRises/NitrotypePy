from typing import TypedDict
from ..basic_object import Options


Car = TypedDict(
    "Car",
    {
        "id": int,
        "carID": int,
        "name": str,
        "longDescription": str,
        "options": Options,
        "enterSound": str,
        "price": int,
        "lastModified": int,
    },
)
