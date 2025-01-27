def make_shirt(tamanho='grande', mensagem='Eu amo Python.'):
    '''Função  que imprime o tamanho e mensagem em camiseta'''
    print(f'\nA camiseta de tamanho: {tamanho}.')
    print(f'Estama com a mensagem: {mensagem}.')


# Chamar camiseta grande com mensagem padrão
make_shirt()

# Chamar camiseta media com mensagem padrão
make_shirt('media')


# Chamar função com com argumentos nomeados
make_shirt(tamanho='pequena', mensagem='Python é fácil de aprender.')
