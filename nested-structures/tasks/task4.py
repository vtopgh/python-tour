cities = {
    'Odesa': {
        'country': 'Ukraine',
        'population': 900000,
    },
    'Dublin': {
        'country': 'Ireland',
        'population': 500000,
    },
}

for city, city_info in cities.items():
    print(city + ': ')
    for key, value in city_info.items():
        print('\t' + key + ': ' + str(value))
