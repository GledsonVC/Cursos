class Employee:
    """Tentativa de criar Funcionario"""
    def __init__(self, nome, sobrenome, salario ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
    

    def give_raise(self, aumento=5_000):
        """Aumento de salario em 5k, ou valor descrito"""
        self.salario += aumento


