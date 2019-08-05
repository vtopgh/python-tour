def city_country(city, country):
    location = city + ', ' + country
    return location.title()


location = city_country('santiago', 'chile')
print(location)
