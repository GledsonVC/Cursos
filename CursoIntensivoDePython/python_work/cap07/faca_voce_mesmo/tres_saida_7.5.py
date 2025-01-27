# usando instrução while
terminal = '\nQual é a sua idade? '
terminal += '\nDigite "quit" para sair do programa: '
idade = ''
while idade != 'quit':
    idade = input(terminal)
    if idade != 'quit':
        idade = int(idade)
        if idade < 3:
            print('Entrada gratúita.')
        elif idade <= 12:
            print(f'Valor do ingresso custa US$10')
        else:
            print(f'Valor do ingresso custa US$15')
print('Fim instrução WHILE')


# usando active
terminal = '\nQual é a sua idade? '
terminal += '\nDigite "quit" para sair do programa: '
active = True
while active:
    idade = input(terminal)
    if idade != 'quit':
        idade = int(idade)
        if idade < 3:
            print('Entrada gratúita.')
        elif idade <= 12:
            print(f'Valor do ingresso custa US$10')
        else:
            print(f'Valor do ingresso custa US$15')
    else:
        active = False
print('Fim ACTIVE')


# usando o break
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
print('Fim BREAK')
