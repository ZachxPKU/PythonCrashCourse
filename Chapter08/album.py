def make_album(artist, title, tracks=None):
    if tracks:
        album_dict = {'artist': artist.title(),
                      'title': title.title(),
                      'tracks': tracks}
    else:
        album_dict = {'artist': artist.title(),
                      'title': title.title()}
    return album_dict


album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)