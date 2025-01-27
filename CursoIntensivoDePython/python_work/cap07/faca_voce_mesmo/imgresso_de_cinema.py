mensagem = '\nQual é a sua idade? '
mensagem += '\nDigite "quit" para sair do programa: '
while True:
    idade = input(mensagem)
    if idade == 'quit':
        break
    else:
        idade = int(idade)
        if idade < 3:
            print('Entrada gratúita.')
        elif idade <= 12:
            print(f'Valor do ingresso custa US$10')
        else:
            print(f'Valor do ingresso custa US$15')
