def make_album(nome_artista, titulo_album, num_musica=None):
    album_de_musica = {'artista': nome_artista, 'album': titulo_album}
    if num_musica:
        album_de_musica['num_musica'] = num_musica
    return album_de_musica

# 3 albuns de musicas
album1 = make_album('pink floyd', 'the wall')
print(album1)
album2 = make_album('beatles', 'the beatles')
print(album2)
album3 = make_album('eagle', 'their greatest hits (1971–1975)')
print(album3)
# Album com quantidade de musicas
album_musica = make_album('Michael Jackson', 'Thriller', 9)
print(album_musica)
