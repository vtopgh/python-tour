def make_album(artist_name, album_name):
    album_info = {'artist_name': artist_name, 'album_name': album_name}
    return album_info


while True:
    print("Press 'q' at any time to continue")

    artist_name = input('Enter artist name:\n')
    if artist_name == 'q':
        break

    album_name = input("Enter album name:\n")
    if album_name == 'q':
        break

    album_info = make_album(artist_name, album_name)
    print(album_info)