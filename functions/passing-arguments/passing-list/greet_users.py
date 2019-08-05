def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name + '!'
        print(msg)


usernames = ['user1', 'user2', 'user3']
greet_users(usernames)