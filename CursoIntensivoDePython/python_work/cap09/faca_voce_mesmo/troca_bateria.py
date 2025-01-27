class Car:
    """Simples tentativa de representar um caroo"""

    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
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

    def fill_gas_tank(self):
        """Exibe mensagem da quantidade padrão de um tanque de gasolina"""
        print(f"Carro comum contem em média 55 litros.")


class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size=40):
        """Iniciando os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da baterria"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa 
        bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """
        Verifica se a bateria é de 65, se não for ele troca o valor para da 
        bateria para 65 fazendo um upgrade.
        """
        if self.battery_size != 65:
            self.battery_size = 65
            print(f'Parabéns, acaba de fazer um upgrade na bateria.\n'
                  f'Sua bateria agora contem {self.battery_size}-kWh')


class EletricCar(Car):
    """Representa aspectos de um carro, específicos para veículos elétricos"""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Carros eletricos não tem tanques de gasolina"""
        print("This car doesn´t have a gas tank!")


carro_eletrico = EletricCar('renaut', 'kwid e-tech', 2024)
print(carro_eletrico.get_descriptive_name())
carro_eletrico.battery.get_range()
carro_eletrico.battery.upgrade_battery()
carro_eletrico.battery.get_range()
