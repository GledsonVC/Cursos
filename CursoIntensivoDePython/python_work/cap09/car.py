# Programa-07
"""Classe que pode ser usada para representar um carro"""
# Programa-01
class Car:
    """Simples tentativa de representar um carro"""

    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        # Programa-02
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # Programa-02
    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro. em milhas"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Programa-04
    def update_odometer(self, mileage):
        # Programa-04
        # """Define a leitura do hodometro para o valor fornecido."""
        # self.odometer_reading = mileage

        # Programa-05
        """
        Define a leitura do hodometro para o valor fornecido.
        Rejeita a alteração se houver tentativa de reverter o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can´t roll back an osometer!")

    # Programa-06
    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles
        # Teste pessoal acerto da função para verificar se está colocando
        # valores negativo utilizando a update_odometer() que já avaliará se o 
        # hodômetro ficará com valor menor ao existente
        # self.update_odometer(miles + self.odometer_reading)



print(80 * '-')
print('\nPrograma-1')
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
print(80 * '-')


print('\nPrograma-2')
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print(80 * '-')

print('\nPrograma-3')
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print(80 * '-')

print('\nPrograma-4')
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
print(80 * '-')

# Teste pessoal do método update_odometer para tentar diminuir não está no livro
print('\nPrograma-5')
my_new_car.read_odometer()
my_new_car.update_odometer(22)
my_new_car.read_odometer()
print(80 * '-')

print('\nPrograma-6')
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
print(80 * '-')
