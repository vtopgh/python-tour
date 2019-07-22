guests = ['guest1', 'guest2', 'guest3']

print("Inviting.." + guests[0])
print("Inviting.." + guests[1])
print("Inviting.." + guests[2])

denied_guest = guests.pop(1)
print("Denied.." + denied_guest)

guests.append('guest4')
print(guests)

guests.insert(0, 'guest')
guests.insert(1, 'guest5')
guests.append('guest6')
print(guests)

denied_guest = guests.pop()
print('Sorry ' + denied_guest)
denied_guest = guests.pop()
print('Sorry ' + denied_guest)
denied_guest = guests.pop()
print('Sorry ' + denied_guest)
denied_guest = guests.pop()
print('Sorry ' + denied_guest)

print(guests)

del guests[1]
del guests[0]
print(guests)

