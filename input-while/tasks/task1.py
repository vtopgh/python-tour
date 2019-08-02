sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(current_sandwich + ' is ready')
    finished_sandwiches.append(current_sandwich)

print('\nFinished sandwiches')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)