def make_album(artist, album, tracks=''):
    album_info = {'artist': artist, 'album': album}
    if tracks:
        album_info['tracks'] = tracks
    return album_info


print(make_album('Metallica', '...And Justice For All'))
print(make_album('Metallica', 'Death Magnetic', tracks='12'))
