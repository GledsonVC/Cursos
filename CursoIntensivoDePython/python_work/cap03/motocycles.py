print('\n01')
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)

print('\n02')
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles.append('ducati')
print(motocycles)

print('\n03')
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

print('\n04')
motocycles = ['honda', 'yamaha', 'suzuki']
motocycles.insert(0, 'ducati')
print(motocycles)

print('\n05')
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[0]
print(motocycles)

print('\n06')
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[1]
print(motocycles)

print('\n07')
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

print('\n08')
motocycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop()
print(f"The last motocycle I owned was a {last_owned.title()}.")

print('\n09')
motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)
motocycles.remove('ducati')
print(motocycles)

print('\n10')
motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocycles)
too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')
