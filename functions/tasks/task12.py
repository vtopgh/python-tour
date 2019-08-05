def make_car(manufacturer, model, **car_info):
    car = {}

    car['manufacturer'] = manufacturer
    car['model'] = model

    for key, val in car_info.items():
        car[key] = val

    return car


car = make_car('mitsubishi', 'evolution lancer X',
               color='blue',
               full_kit=True)
print(car)