print('\nPrograma-01')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print('\nPrograma-02')
alien_0 = {'color': 'green'}
print(alien_0['color'])

print('\nPrograma-03')
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print('\nPrograma-04')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('\nPrograma-05')
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

print('\nPrograma-06')
alien_0 = {'color': 'green', 'points': 5}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print('\nPrograma-07')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Desloca o alienígena para direita
# Estipula a distância que o alienígena deve percorrer conforme sua velocidade
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Com isso, o alienigena fica veloz
    x_increment = 3
# A posição nova é a posição antiga mais o incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print('\nPrograma-08')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print('\nPrograma-09')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print('\nPrograma-10')
# Cria uma lista vazia para armazenar alienígenas
aliens = []
# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alian = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alian)
# Exibe os primeiros 5 alienigenas
for alien in aliens[:5]:
    print(alien)
print("...")
# Exibe quantos alieans foram criados
print(f"Total number of aliens: {len(aliens)}")

print('\nPrograma-11')
# Cria uma lista vazia para armazenar alienígenas
aliens = []
# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alian = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alian)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Exibe os primeiros 5 alienigenas
for alien in aliens[:5]:
    print(alien)
print("...")

print('\nPrograma-12')
# Cria uma lista vazia para armazenar alienígenas
aliens = []
# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alian = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alian)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Trocando 7 alienigenas se for verde muda para amarelo 
# e se for amarelo para red e seus valores
for alien in aliens[0:7]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:10]:
    print(alien)
print("...")
