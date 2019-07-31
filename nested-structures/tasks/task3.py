favorite_places = {
    'Dublin': ['user1', 'user2'],
    'Dakota': ['user4', 'user3'],
}

for location, user_info in favorite_places.items():
    print(location + ':')
    for user in user_info:
        print('\t' + user)