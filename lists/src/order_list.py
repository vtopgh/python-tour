# sort() changes initial order
vehicles = ['jet', 'moto', 'spaceship', 'car']
vehicles.sort()
print(vehicles)

vehicles.sort(reverse=True)
print(vehicles)

# sorted() doesn't change initial order
vehicles = ['jet', 'moto', 'spaceship', 'car']
print(sorted(vehicles))
print(sorted(vehicles, reverse=True))
print(vehicles)

# reverse() in reverse order
vehicles.reverse()
print(vehicles)

# list length
print(len(vehicles))