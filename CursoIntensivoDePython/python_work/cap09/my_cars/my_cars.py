print(80 * '-')
print('\nPrograma-1')
from car import Car, EletricCar
my_mustang = Car('ford', 'mustang', 2025)
print(my_mustang.get_descriptive_name())
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print(80 * '-')

print('\nPrograma-2')
import car
my_mustang = car.Car('ford', 'mustang', 2025)
print(my_mustang.get_descriptive_name())
my_leaf = car.EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print(80 * '-') 
