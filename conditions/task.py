# TASK 1
alien_color = 'red'
if alien_color == 'green':
    print('5 points')

if alien_color != 'green':
    pass

# TASK 2
if alien_color != 'green':
    print('5 points')
else:
    print('10 points')

# TASK 3
if alien_color == 'green':
    print('5 points')
elif alien_color == 'yellow':
    print('10 points')
else:
    print('15 points')

# TASK 4
age = 65
if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('Baby')
elif age >= 4 and age < 13:
    print('child')
elif age >= 13 and age < 20:
    print('big child')
elif 20 <= age < 65:
    print('adult')
else:
    print('elder')

# TASK 5
favorite_fruits = ('banana', 'orange', 'apple')
if 'banana' in favorite_fruits:
    print('banana')
if 'cocos' in favorite_fruits:
    print('cocos')
if 'orange' in favorite_fruits:
    print('orange')
if 'apple' in favorite_fruits:
    print('apple')

