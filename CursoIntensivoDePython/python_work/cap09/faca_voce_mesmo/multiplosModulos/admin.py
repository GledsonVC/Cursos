import user
from privileges import Privileges


class Admin(user.User):
    """Cria subclasse User para administrador"""

    def __init__(self, first_name, last_name, senha):
        super().__init__(first_name, last_name, senha)
        self.privileges = Privileges()


admin = Admin('gledson', 'vasconcellos cavalheiro', 'admin123')
admin.privileges.show_privileges()
