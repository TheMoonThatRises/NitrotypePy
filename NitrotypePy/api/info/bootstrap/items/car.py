from NitrotypePy.api.info.bootstrap import bootstrap

def car(car_id = 0):
    car_list = bootstrap.bootstrap('cars')

    for car in car_list:
        if car['id'] == car_id:
            return car

    return False
