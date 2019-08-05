def show_jets(jets):
    for jet in jets:
        print(jet)


def make_great(jets):
    '''
    # using list-generator
    great_jets = ['Great ' + jet for jet in jets]
    return great_jets
    '''

    # or

    for jet in range(len(jets)):
        jets[jet] += ' is great!'


jets = ['f-18', 'f-86', 'me-163']
show_jets(jets)
make_great(jets)
show_jets(jets)