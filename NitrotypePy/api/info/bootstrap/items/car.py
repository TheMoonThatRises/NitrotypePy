from .....objects.api.info.bootstrap.item.car import Car
from ..bootstrap import bootstrap
from typing import List, Union


def car(car_id=0) -> Union[Car, List[Car], bool]:
    car_list = bootstrap('cars')

    if car_id:
        for car in car_list:
            if car['id'] == car_id:
                return car
    else:
        return car_list

    return False
