mensagem = '\nEntre com dois números e o programa fara a soma deles.'
mensagem += '\nPrecione "s" para sair do programa.\n'
print(mensagem)
while True:
    try:
        num1 = input('Digite o primeiro número: ')
        if num1 == 's':
            break
        num1 = int(num1)

        num2 = input('Digite o segundo número: ')
        if num2 == 's':
            break
        num2 = int(num2)
    except ValueError:
        print('Por favor, insira apenas número.\n')
    else:
        print(f'A soma de {num1} + {num2} = {num1+num2}\n')
