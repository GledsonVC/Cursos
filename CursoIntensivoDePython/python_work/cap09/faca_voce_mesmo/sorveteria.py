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


class IceCreamStand(Restaurante):
    """Definindo uma subclasse sorveteria de Restaurante"""

    def __init__(self, restaurant_name, cuisine_type='sorveteria'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'chocomenta', 'doce de leite', 'flocos', 'amindoim', 'creme',
            'chocolate', 'morango', 'coco', 'creme de avelã', 'maracujá',
            'passas ao rum', 'napolitano', 'milho', 'cookies e creme', 'açaí',
            'café',
        ]

    def sabores(self):
        """Retorna a lista de sabores"""
        print(f"Sabores de sorvete da sorveteria "
              f"{self.restaurant_name.title()}:")
        for sabor in self.flavors:
            print(f"\t-{sabor.upper()}")


# instancia de sorveteria
sorveteria = IceCreamStand('bacio di latte')
print("\n")
sorveteria.sabores()
sorveteria.describe_restaurant()
print("\n")
