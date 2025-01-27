# Fatia do primeiro indice da lisa ao terceiro
print('\nPrograma-01')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Fatia do segundo indice da lista ao quarto
print('\nPrograma-02')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# Fatia do primeiro indice da lista ao quarto omitindo no range o primeiro indice
print('\nPrograma-03')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# Fatia do terceiro indice da lista até o final dela omitindo no range o ultimo indice
print('\nPrograma-04')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# Fatia mostrando tres ultimos players da lista
print('\nPrograma-05')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# Imprimindo 3 primeiros jogadores com loop for
print('\nPrograma-06')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
