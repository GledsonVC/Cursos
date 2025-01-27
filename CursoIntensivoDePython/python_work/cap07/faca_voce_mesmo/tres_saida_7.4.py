# usando instrução while
mensagem = '\nInforme os ingredientes de sua pizza!'
mensagem += '\nDigite "quit" para sair: '
ingrediente = ''
while ingrediente != 'quit':
    ingrediente = input(mensagem)
    if ingrediente != 'quit':
        print(f'\nIngrediente {ingrediente} adcionado a pizza.')
print('Fim instrução WHILE')


# usando active
mensagem = '\nInforme os ingredientes de sua pizza!'
mensagem += '\nDigite "quit" para sair: '
active = True
while active:
    ingrediente = input(mensagem)
    if ingrediente != 'quit':
        print(f'\nIngrediente {ingrediente} adcionado a pizza.')
    else:
        active = False
print('Fim ACTIVE')


# usando o break
while True:
    mensagem = '\nInforme os ingredientes de sua pizza!'
    mensagem += '\nDigite "quit" para sair: '
    ingrediente = input(mensagem)
    if ingrediente != 'quit':
        print(f'\nIngrediente {ingrediente} adcionado a pizza.')
    else:
        break
print('Fim BREAK')
