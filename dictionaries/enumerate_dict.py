nums = {
    'one': 1,
    'two': 2,
    'three': 3,
}

# enumerate key and value
for key, value in nums.items():
    print(key + str(value))

# enumerate key
for key in nums:
    print(key)

# or
for key in nums.keys():
    print(key)

# enumerate values
for value in nums.values():
    print(value)
