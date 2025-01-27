class Restaurante:
    """Definindo uma classe para Restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        """Definindo atributo nome do restaurante e tipo de cozinha"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        """Exibe nome e tipo de cozinha do restaurante"""
        print(f'Restaurante: {self.restaurant_name.title()}.')
        print(f'Tipo de cozinha: {self.cuisine_type}.')
    
    def open_restaurant(self):
        """Exibe que o restaurante do nome X está aberto"""
        print(f'O restaurante {self.restaurant_name.title()} está aberto!')
