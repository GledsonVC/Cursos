# Variavel constante + Pergunta 
VAR = int(237)
print(f'\nVamos ao {VAR}?')

# Pega dados do usuário em string+minuscula 
# com a pergunta e atribui a variavel
resposta = str.lower(input('Resposta (S/N): '))

# variavel pegando apenas a primeira letra
resposta = resposta[0]

# Loop verificação de resposta se foi 'S' ou 'N'
# e faz novamente a pergunta
while resposta not in 'sn':
    print(f'\n"{resposta}" não é um dado válido')
    print('Responda Sim ou Não!')
    print(f'\nVamos ao {VAR}?')
    # com a pergunta e atribui a variavel
    resposta = str.lower(input('Resposta S/N: '))
    # variavel pegando apenas a primeira letra
    resposta = resposta[0]

# Condição e "saudação" se verdade ou "decepção" se for Falso
if (resposta == 's'): # Verdade
    print(f'\nEsse é um computeiro de verdade bora programar no {VAR}!')
else:
    print(f'\nSe não for ao {VAR}, nunca será um computeiro')

# Fim do programa com Mensagem
print('\nFim do programa\n\n')
