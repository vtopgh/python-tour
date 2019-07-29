current_users = ['user1', 'user3', 'user5', 'user2', 'user4']
new_users = ['user10', 'user11', 'user3', 'user1']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('Choose another name')
    else:
        print('Enter new name')