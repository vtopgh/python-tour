def describe_pet(pet_name, animal_type='dog'):
    print('She has a ' + animal_type)
    print("Her " + animal_type + "'s name is " + pet_name.title())


# python interprets this arg as positional
describe_pet(pet_name='willie')
describe_pet('willie')
# animal_type is defined, python ignores default arg value animal_type='dog'
describe_pet(pet_name='harry', animal_type='hamster')

'''
^---NOTE---^
If we use default values, all parameters with a default value must
follow parameters that have no default values. This is necessary in order
for python to correctly interpret positional arguments.
'''
