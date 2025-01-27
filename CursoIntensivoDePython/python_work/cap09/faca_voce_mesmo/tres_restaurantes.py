class Restaurante:
    """Definindo uma classe para Restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        """Definindo atributo nome do restaurante e tipo de cozinha"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Exibe nome e tipo de cozinha do restaurante"""
        print(f'\nRestaurante: {self.restaurant_name.title()}.')
        print(f'Tipo de cozinha: {self.cuisine_type}.')

    def open_restaurant(self):
        """Exibe que o restaurante do nome X está aberto"""
        print(f'O restaurante {self.restaurant_name.title()} está aberto!')


# Instanciando 3 restaurantes
resaurante1 = Restaurante('sushi jardim brasil', 'japonesa')
resaurante2 = Restaurante('almanara', 'arabe')
resaurante3 = Restaurante('sí señor', 'mexicana')

# Chamando o método describe_restaurant para os 3 restaurantes
resaurante1.describe_restaurant()
resaurante2.describe_restaurant()
resaurante3.describe_restaurant()
