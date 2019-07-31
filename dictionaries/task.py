# TASK 1
person = {
    'first_name': 'person_fname',
    'last_name': 'person_lname',
    'age': 'person_age',
    'city': 'person_city',
}

for value in person.values():
    print(value)

# TASK 2
favorite_nums = {
    'person1': 1,
    'person2': 2,
    'person3': 3,
    'person4': 4,
}

for key, value in favorite_nums.items():
    print(key + ': ' + str(value))

# by default the same result without keys()
for key in favorite_nums.keys():
    print(key)

for value in favorite_nums.values():
    print(value)
