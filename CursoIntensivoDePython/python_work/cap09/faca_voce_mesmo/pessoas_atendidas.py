class Restaurante:
    """Definindo uma classe para Restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        """Definindo atributo nome do restaurante e tipo de cozinha"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    

    def describe_restaurant(self):
        """Exibe nome e tipo de cozinha do restaurante"""
        print(f'Restaurante: {self.restaurant_name.title()}.')
        print(f'Tipo de cozinha: {self.cuisine_type}.')
    
    def open_restaurant(self):
        """Exibe que o restaurante do nome X está aberto"""
        print(f'O restaurante {self.restaurant_name.title()} está aberto!')
    
    def imprime_quantidade_clientes_atendido(self):
        print(f'O restaurante {self.restaurant_name.title()} atendeu '
      f'{self.number_served} pessoas.')
    
    def set_number_served(self, numero_de_clientes_atendido):
        """Define a quantidade de pessoas atendidas"""
        self.number_served = numero_de_clientes_atendido
    
    def increment_number_served(self, adciona_cliente):
        """
        Verifica se o valor é superior as que já foram atendidas.
        Incrementa quantidade de pessoas atendida se positivo ou imprime na tela
        que não pode diminuir a quantidade de pessoas que já foram atendidas.
        """
        if self.number_served + adciona_cliente > self.number_served:
            self.number_served += adciona_cliente
        else:
            print('Não pode diminuir a quantidade de pessoas que já foram '
                  'atendidas.')

# Instanciando variável restaurante
resaurante = Restaurante('sushi jardim brasil', 'japonesa')

# Imprime quantidade de pessoas atendidas, altera quantidade e imprime novamente
resaurante.imprime_quantidade_clientes_atendido()
resaurante.number_served = 123
resaurante.imprime_quantidade_clientes_atendido()

# Chama o método set_number_served() que permite alterar o valro de possoas 
# atendidas e imprime o valor
resaurante.set_number_served(234)
resaurante.imprime_quantidade_clientes_atendido()

# Chamar o método increment_number_served com um valor e imprimendo na tela
resaurante.increment_number_served(6)
resaurante.imprime_quantidade_clientes_atendido()
# Teste pessoal tentando diminuir a quantidade de clientes atendido
resaurante.increment_number_served(-10)
resaurante.imprime_quantidade_clientes_atendido()
