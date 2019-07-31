buddy = {'animal_type': 'cat', 'owner': 'john'}
oscar = {'animal_type': 'dog', 'owner': 'jadden'}

pets = [buddy, oscar]

for pet in pets:
    print("Animal type is: " + pet['animal_type'])
    print("Owner is: " + pet['owner'])