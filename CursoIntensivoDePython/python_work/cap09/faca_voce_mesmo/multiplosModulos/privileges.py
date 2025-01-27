class Privileges:
    """Classe de privilegios de usuários"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Imprime em tela enumerando a lista de privilégios do adm"""
        # loop para imprimir 'numero de privilégio': 'privilégio'
        if self.privileges:
            print("\nPrivilégio de um administrador: ")
            for chave in range(0, len(self.privileges)):
                print(f"{chave+1}: {self.privileges[chave]}")
        else:
            print('Não tem privilégios')
