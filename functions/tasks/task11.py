def build_profile(first, last, **user_info):
    user_profile = {}

    user_profile['first_name'] = first
    user_profile['last_name'] = last

    for key, value in user_info.items():
        user_profile[key] = value

    return user_profile


my_profile = build_profile('Volodymyr', 'T.',
                           location='Odessa, UA',
                           age=21,
                           hobbies=['programming', 'music', 'psychological books', 'jet aviation'])
print(my_profile)