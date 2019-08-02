sandwich_orders = ['sandwich1', 'pastrami', 'pastrami', 'sandwich2', 'sandwich3', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(current_sandwich + ' is ready')
    finished_sandwiches.append(current_sandwich)

print('\nFinished sandwiches')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)