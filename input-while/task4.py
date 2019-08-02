active = True
while active:
    ingredient = input('Add some ingredients:\n')
    if ingredient == 'quit':
        active = False
    else:
        print(ingredient + ' is added to pizza')