vehicles = ['jet', 'moto', 'spaceship', 'car']
for vehicle in vehicles:
    print(vehicle)

# Create num lists

# range()
for value in range(1, 5):
    print(value)

# using range() for creating num lists
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# statistics with numeric lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))