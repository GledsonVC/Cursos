from random import choice

def sorteio():
    num_e_letras_sorteio = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd'
        ]
    resultado_sorteio = list()
    while len(resultado_sorteio) != 4:
        caracter_sorteado = choice(num_e_letras_sorteio)
        if caracter_sorteado not in resultado_sorteio:
            resultado_sorteio.append(caracter_sorteado)
    return sorted(resultado_sorteio)

# meu bilhete
my_ticket = sorteio()
print(f'\nMeu ticket é:\n{my_ticket}')

# loop para verificar quantas vezes será necessário para o bilhete ser premiado
resultado = 1
while my_ticket != sorteio():
    resultado += 1
print(f'Precisou {resultado} sorteios para seu ticket ser premiado.\n')
