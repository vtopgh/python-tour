# TASK 1
rivers = {
    'Amazonas': 'South America',
    'Nile': 'Egypt',
    'Mississippi': 'USA',
}

for river, location in rivers.items():
    print(river + ' in ' + location)

# TASK 2
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

involved_people = ['jen', 'jozzeph', 'phil', 'annie']

for name in favorite_languages:
    if name not in involved_people:
        print('You should vote ' + name)
    else:
        print('Thanks for voting ' + name)
