def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for complete_models in completed_models:
        print('Completed: ' + complete_models)


unprinted_designs = ['iphone case', 'robot pendant', 'dodeahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
