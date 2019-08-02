cars = {}
active = True

while active:
    name = input("What's your name?\n")
    car = input('Which car would you like to add?\n')
    cars[name] = car

    repeat = input('Would you like to add another car?(y/n)\n')
    if repeat == 'n':
        active = False

print('\n---Results---')
for name, car in cars.items():
    print(name + ' ' + car)