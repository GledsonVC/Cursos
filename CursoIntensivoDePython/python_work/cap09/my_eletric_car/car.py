"""Classe que pode ser usada para representar um carro"""
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
        Rejeita a alteração se houver tentativa de reverter o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can´t roll back an osometer!")


    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles


class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""


    def __init__(self, battery_size=40):
        """Iniciando os atributos da bateria"""
        self.battery_size = battery_size
    

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da baterria"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    

    def get_range(self):
        """Exibe frase sobre a distância que o carro 
        consegue percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class EletricCar(Car):
    """Modela aspectos de um carro, específicos para veículos elétricos."""


    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    
    def describe_battery(self):
        return(self.battery.describe_battery())
    
    
    def fill_gas_tank(self):
        """Carros eletricos não tem tanques de gasolina"""
        print("This car doesn´t have a gas tank!")


