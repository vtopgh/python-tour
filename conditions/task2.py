user_names = ['user1', 'user3', 'admin', 'user2', 'user4']

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print('Hello: ' + user_name + 'would you like to leave ur pos?')
        else:
            print('Hello: ' + user_name)
else:
    print('Need to find some users')
