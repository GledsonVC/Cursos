from car import Car

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
