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
