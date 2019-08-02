car_name = input('Which car would you like?:')
print('Trying to find..' + car_name)

visitors = input('How many visitors?:')
if int(visitors) > 8:
    print('Wait')
else:
    print('Ready')

num = input('Enter num: ')
if int(num) % 10 == 0:
    print(num + ' is multiple to ' + '10')
else:
    print(num + ' is not multiple to ' + '10')