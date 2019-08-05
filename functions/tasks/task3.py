def make_shirt(text='I love Python', shirt_size='L'):
    print('Size: ' + shirt_size + '\n' + 'Text: ' + text)


# value by default
make_shirt()
# args order is important here
make_shirt('Python loves me', 'S')
