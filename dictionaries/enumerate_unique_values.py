favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# output all values without duplicates
for value in set(favorite_languages.values()):
    print(value.title())
