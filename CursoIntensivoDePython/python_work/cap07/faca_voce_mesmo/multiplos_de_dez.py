numero_multiplo_dez = 'Informe um número e irei dizer se ele é multiplo de 10.'
numero_multiplo_dez += '\nInforme o número: '
numero_multiplo_dez = input(numero_multiplo_dez)
numero_multiplo_dez = int(numero_multiplo_dez)
if numero_multiplo_dez % 10 == 0:
    print(f'O numero {numero_multiplo_dez} é multiplo de 10.')
else:
    print(f'O numero {numero_multiplo_dez} não multiplo de 10.')
