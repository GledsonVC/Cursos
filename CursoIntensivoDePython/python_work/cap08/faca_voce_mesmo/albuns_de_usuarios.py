def make_album(nome_artista, titulo_album, num_musica=None):
    album_de_musica = {'artista': nome_artista, 'album': titulo_album}
    if num_musica:
        album_de_musica['num_musica'] = num_musica
    return album_de_musica

print(80 * '-')
while True:
    print('\nDigite o artista, álbum e quantidade de música se desejar.'
          '\nDigite "q" a qualquer momento se deseja sair.')
    artista = input('Digite o nome do artista: ')
    if artista == 'q':
        break
    album = input('Digite o albúm: ')
    if album == 'q':
        break
    qtd_musica = input('Quantidade de música ou digite "0": ')
    if qtd_musica == 'q':
        break
    if qtd_musica == '0':
        album = make_album(artista, album)
        print(album)
    else:
        album = make_album(artista, album, qtd_musica)
        print(album)
print(80 * '-')
