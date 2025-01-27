mensagem = '\nEntre com dois números e o programa fara a soma deles.'
print(mensagem)
try:
    num1 = input('Digite o primeiro número: ')
    num1 = int(num1)
    num2 = input('Digite o segundo número: ')
    num2 = int(num2)
except ValueError:
    print('Por favor, insira apenas número.\n')
else:
    print(f'A soma de {num1} + {num2} = {num1+num2}')
