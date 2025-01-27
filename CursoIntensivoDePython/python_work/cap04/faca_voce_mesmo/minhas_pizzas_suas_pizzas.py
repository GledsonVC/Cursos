pizzas = ['toscana', 'calabresa', '4-queijos']
for pizza in pizzas:
    print(f'Como gosto de pizza de {pizza}.')
print('Como eu amo de pizza.')


# inicio do Exercicio usando o programa anterior
print('\n\n')
friend_pizzas = pizzas[:]
pizzas.append('portuguesa')
friend_pizzas.append('mussarela')
print('\nMinhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza)
print('\nPizzas do meu amigo favoritas são:')
for pizza_amigo in friend_pizzas:
    print(pizza_amigo)
