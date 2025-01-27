print('\n01')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
cars.sort()
print(cars)

print('\n02')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
cars.sort(reverse=True)
print(cars)

print('\n03')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print(cars)

print('\n04')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)
cars.reverse()
print(cars)

print('\n05')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(f'O tamanho da lista {cars} é',len(cars))
