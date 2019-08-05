# An asterisk(*) tells Python to create an empty tuple which will contain all args
def make_pizza(*toppings):
    print('\nMaking pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'peppers', 'cheese')