from .....objects.api.info.bootstrap.item.car import Car
from ..bootstrap import bootstrap
from typing import List, Union


def car(car_id=0) -> Union[Car, List[Car], bool]:
    """Returns information about the car.

    Endpoint: https://www.nitrotype.com/index/624/bootstrap.js

    :param car_id: The car to access from the bootstrap.
    :type car_id: int
    :returns: A dict of information about the car, or False if the car cannot be found.
    :rtype: dict
    """

    car_list = bootstrap("cars")

    if car_id:
        for car in car_list:
            if car["id"] == car_id:
                return car
    else:
        return car_list

    return False
