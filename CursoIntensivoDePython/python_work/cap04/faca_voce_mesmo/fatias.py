# Imprimindo 3 primeiros jogadores com loop for
print('\nPrograma-06')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())


# inicio do Exercicio usando o programa anterior
print('\n\n\nOs três primeiros elementos da lista são:')
print(players[:3])

print('\nOs três elementos que ficam no meio da lista são:')
print(players[1:4])

print('\nOs três últimos elementos da lista são:')
print(players[-3:])
