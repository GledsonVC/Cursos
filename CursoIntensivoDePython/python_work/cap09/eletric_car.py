# Programa-1
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


    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro. em milhas"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """
        Define a leitura do hodometro para o valor fornecido.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can´t roll back an osometer!")


    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles
    
    # Programa-3
    def fill_gas_tank(self):
        """Exibe mensagem da quantidade padrão de um tanque de gasolina"""
        print(f"Carro comum contem em média 55 litros.")

# Programa-4
class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""


    def __init__(self, battery_size=40):
        """Iniciando os atributos da bateria"""
        self.battery_size = battery_size
    

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da baterria"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    # Programa-5
    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa 
        bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    


# Programa-1
class EletricCar(Car):
    """Representa aspectos de um carro, específicos para veículos elétricos"""


    def __init__(self, make, model, year):
        # Programa-1 
        # """Inicializa os atributos da classe-pai"""
        # super().__init__(make, model, year)
        
        # Programa-2 
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico. 
        """
        super().__init__(make, model, year)
        # Programa-1
        # self.battery_size = 40
        # Programa-4
        self.battery = Battery()
    
    # Programa-2
    def describe_battery(self):
        #     """Exibe uma frase descrevendo o tamanho da bateria"""
        #     print(f"This car has a {self.battery_size}-kWh battery.")
        # Teste pessoal para chamada de describe_battery apontando para classe
        # Battery usando a função describe_battery, necessário para manter 
        # funcionando o programa 2 e 3
        return(self.battery.describe_battery())
    
    # Programa-3
    def fill_gas_tank(self):
        """Carros eletricos não tem tanques de gasolina"""
        print("This car doesn´t have a gas tank!")


print(80 * '-')
print('\nPrograma-1')
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name()) 
print(80 * '-')

print('\nPrograma-2')
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
print(80 * '-')

# Teste pessoal definido como Programa-3
print('\nPrograma-3')
my_leaf = EletricCar('nissan', 'leaf', 2024)
my_leaf.fill_gas_tank()
print(80 * '-')

print('\nPrograma-4')
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
print(80 * '-')

print('\nPrograma-5')
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print(80 * '-')
