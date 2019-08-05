def show_jets(jets):
    for jet in jets:
        print(jet)


def make_great(jets):
    for jet in range(len(jets)):
        jets[jet] += ' is great!'
    return jets


jets = ['f-18', 'f-86', 'me-163']
show_jets(jets)
new_jets = make_great(jets[:])
show_jets(new_jets)
