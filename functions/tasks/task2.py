def make_shirt(shirt_size, text):
    print('Size: ' + shirt_size + '\n' + 'Text: ' + text)


# positional args
make_shirt('S', 'Python')
# named args
make_shirt(shirt_size='S', text='Python')
