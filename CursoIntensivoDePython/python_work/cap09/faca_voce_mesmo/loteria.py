from random import choice

num_e_letras_sorteio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 'a', 'b', 'c', 'd']
resultado_sorteio = list()
while len(resultado_sorteio) != 4:
    caracter_sorteado = choice(num_e_letras_sorteio)
    if caracter_sorteado not in resultado_sorteio:
        resultado_sorteio.append(caracter_sorteado)
print(resultado_sorteio)
