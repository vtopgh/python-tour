def get_sandwich_components(*components):
    print('Sandwich component:')
    for component in components:
        print('-' + component)

get_sandwich_components('cheese')
get_sandwich_components('onion', 'pepper')
