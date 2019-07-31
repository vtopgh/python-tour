# Tuples cant be changed
# Elements cant be changed, but we can assign new value to tuple's variable

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 -> error

for dimension in dimensions:
    print(dimension)

# Tuple replacement
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
