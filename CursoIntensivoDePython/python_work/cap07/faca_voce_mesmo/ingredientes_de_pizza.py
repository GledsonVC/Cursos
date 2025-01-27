while True:
    mensagem = '\nInforme os ingredientes de sua pizza!'
    mensagem += '\nDigite "quit" para sair: '
    ingrediente = input(mensagem)
    if ingrediente != 'quit':
        print(f'\nIngrediente {ingrediente} adcionado a pizza.')
    else:
        break
