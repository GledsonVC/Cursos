class User:
    """Criando uma classe de usuários"""
    def __init__(self, first_name, last_name, senha):
        """Parâmetros nome, sobrenome e senha"""
        self.first_name = first_name
        self.last_name = last_name
        self.senha = senha
    

    def describe_user(self):
        """Exibe nome completo do usuário formatado"""
        print(f'Nome: {self.first_name.title()}')
        print(f'Sobrenome: {self.last_name.title()}')
    
    def greet_user(self):
        """Saudação para o usuário"""
        print(f'\nSeja bem vindo {self.first_name.title()}.')
    


user1 = User('gledson', 'vasconcellos cavalheiro', 'gle123')
user1.greet_user()
user1.describe_user()

user2 = User('ellen', 'yonobi cavalheiro', 'e123')
user2.greet_user()
user2.describe_user()

user3 = User('luan', 'yonobi cavalheiro', 'lu123')
user3.greet_user()
user3.describe_user()

user4 = User('zoraide', 'vasconcellos cavalheiro', 'zo123')
user4.greet_user()
user4.describe_user()
