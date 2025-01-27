def make_shirt(tamanho, mensagem):
    '''Função  que imprime o tamanho e mensagem em camiseta'''
    print(f'\nA camiseta de tamanho: {tamanho}.')
    print(f'Estama com a mensagem: {mensagem}.')


# Chamar função com argumentos posicionais
make_shirt('pequeno', 'Sou programador PYTHON')

# Chamar função com com argumentos nomeados
make_shirt(mensagem='Garoto de programa', tamanho='grande')
