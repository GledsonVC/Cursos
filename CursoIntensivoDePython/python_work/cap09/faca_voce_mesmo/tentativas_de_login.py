class User:
    """Criando uma classe de usuários"""
    def __init__(self, first_name, last_name, senha):
        """Parâmetros nome, sobrenome e senha"""
        self.first_name = first_name
        self.last_name = last_name
        self.senha = senha
        self.login_attempts = 0
    

    def describe_user(self):
        """Exibe nome completo do usuário formatado"""
        print(f'Nome: {self.first_name.title()}')
        print(f'Sobrenome: {self.last_name.title()}')
    
    def greet_user(self):
        """Saudação para o usuário"""
        print(f'\nSeja bem vindo {self.first_name.title()}.')
    
    def increment_login_attempts(self):
        """Incrementa 1 a login_attempts"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reseta quantidade de login_attempts a 0"""
        self.login_attempts = 0
    
    def imprime_quantidade_login_attempts(self):
        print(f'Tentativa {self.login_attempts} de login de a conta de '
              f'{self.first_name.title()}')
  

# Criação de instancia de usuário
user = User('gledson', 'vasconcellos cavalheiro', 'gle123')
# Tentativa de login e impressão 3 vezes
user.increment_login_attempts()
user.imprime_quantidade_login_attempts()
user.increment_login_attempts()
user.imprime_quantidade_login_attempts()
user.increment_login_attempts()
user.imprime_quantidade_login_attempts()
# Reset de quantidade de login
user.reset_login_attempts()
user.imprime_quantidade_login_attempts()
