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


class Admin(User):
    """Cria subclasse User para administrador"""

    def __init__(self, first_name, last_name, senha):
        super().__init__(first_name, last_name, senha)
        self.privileges = Privileges()

class Privileges:
    """Classe que mostra os privilegios de um usuário admin""" 

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]  
    
    def show_privileges(self):
        """Imprime em tela enumerando a lista de privilégios do adm"""
        # loop para imprimir 'numero de privilégio': 'privilégio'
        print("\nPrivilégio de um administrador: ")
        if self.privileges:
            for chave in range(0, len(self.privileges)):
                print(f"{chave+1}: {self.privileges[chave]}")
        else:
            print('Não tem privilegios')


admin = Admin('gledson', 'vasconcellos cavalheiro', 'admin123')
admin.privileges.show_privileges()
admin.privileges.privileges = []
admin.privileges.show_privileges()
