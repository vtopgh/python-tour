def show_jets(jets):
    for jet in jets:
        print(jet)


def delete_jets(jets):
    while jets:
        current_jet = jets.pop()
        print('Removed: ' + current_jet)


jets = ['f-18', 'f-86', 'me-163']
show_jets(jets)
delete_jets(jets[:])
show_jets(jets)