cars =  ['audio', 'bmw', 'subaru', 'toyota']
print('\nCarros que pertence a lista são:')
for car in cars:
    if car.upper() == 'BMW':
        print(car.upper())
    else:
        print(car.title())

car1 = 'subaru'
car2 = 'BMW'
car3 = 'mustang'
car4 = 'ferrari'

if (car1 in cars) and (car2.lower() in cars):
    print(f'\n{car1.title()} (e) {car2} estão na lista!')
else:
    print(f'\n{car1.title()} (e) {car2} não estão na lista!')

if (car2 in cars) and (car3 in cars):
    print(f'{car2.upper()} (e) {car3.title()} estão na lista!')
else:
    print(f'{car2.upper()} (e) {car3.title()} não estão na lista!')

if (car1 in cars) or (car4 in cars):
    print(f'{car1.title()} (ou) {car4.title()} estão na lista!')
else:
    print(f'{car1.title()} (ou) {car4.title()} não estão na lista!')

if (car3 in cars) or (car4 in cars):
    print(f'{car3.title()} (ou) {car4.title()} estão na lista!')
else:
    print(f'{car3.title()} (ou) {car4.title()} não estão na lista!')
