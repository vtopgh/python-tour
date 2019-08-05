'''
Sometimes program has to get arbitrary set of arguments,
but you do not know in advance which kind of information passes.
In this sample we have first two required args which always get name and surname,
and also third arg can get arbitrary set of named args.

Third arg allows us to pass any quantity 'name-value' pair.
Two asterisk tells Python to create an empty dict and insert all getting 'name-value' pair to this one.
'''

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)