while True:
    age = input('Enter your age: ')
    if int(age) < 3:
        print('Free')
    elif 3 <= int(age) <= 12:
        print('10$')
    else:
        print('$15')