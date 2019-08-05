def describe_pet(animal_type, pet_name):
    print('She has a ' + animal_type)
    print("Her " + animal_type + "'s name is " + pet_name.title())


# Named argument is a name-value pair and now we can pass arguments in any order
describe_pet(animal_type='hamster', pet_name='harry')
