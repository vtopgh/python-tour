# creating slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[-3:])

# from begin
print(players[:4])

# till the end
print(players[0:])

print("First three players:")
for player in players[:3]:
    print(player.title())

# COPYING THE LIST [:]
my_foods = ['pizza', 'banana', 'meat']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)


