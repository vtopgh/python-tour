# Create list
colors = ['blue', 'yellow', 'white']

# Aces list
print(colors)
print(colors[0])
# -1 = Always last item, -2 = last item - 1
print(colors[-1])

# Change item in list
colors[0] = 'blue_ch'
print(colors)

# Add item to list

# append item to end of list
colors.append('black')
print(colors)

# insert item to list 'insert(index, item)'
colors.insert(4, 'green')
print(colors)
# all items are shifting >> by 1
colors.insert(2, 'red')
print(colors)

# Remove item from list
del colors[2]
print(colors)

# Remove last item using pop()
removed_item = colors.pop()
print(colors)
print(removed_item)

# Remove using pop() by index
second_color = colors.pop(1)
print(colors)
print(second_color)
# if we don't need removed item anymore we use operator del
# if we need we use pop()

# Remove item remove() by value if we don't know index
colors.remove('blue_ch')
print(colors)
# remove() deleting only first entry given value 