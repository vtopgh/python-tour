# dict
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra'],
}

print('You ordered a ' + pizza['crust'] + ' with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)