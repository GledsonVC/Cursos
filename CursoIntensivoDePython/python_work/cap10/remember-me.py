from pathlib import Path
import json


# print('\nPrograma-01')
# username = input("What is your name: ")
# # path = Path('.\\cap10\\username.json')
# # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
# path = Path(__file__).parent/'username.json'
# contents = json.dumps(username)
# path.write_text(contents)
# print(f"We'll remember you when you come back, {username}!")


# print('\nPrograma-02')
# # path = Path('.\\cap10\\username.json')
# # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
# path = Path(__file__).parent/'username.json'
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}")
# else:
#     username = input("What is your name: ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")


# print('\nPrograma-03')
# def greet_user():
#     """Cumprimenta o usuário pelo nome"""
#     # path = Path('.\\cap10\\username.json')
#     # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
#     path = Path(__file__).parent/'username.json'
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}")
#     else:
#         username = input("What is your name: ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
# greet_user()

# print('\nPrograma-03')
# def greet_user():
#     """Cumprimenta o usuário pelo nome"""
#     # path = Path('.\\cap10\\username.json')
#     # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
#     path = Path(__file__).parent/'username.json'
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}")
#     else:
#         username = input("What is your name: ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
# greet_user()

# print('\nPrograma-04')
# def get_stored_username(path):
#     """Obtém o nome de usuário armazenado , se disponível"""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None

# def greet_user():
#     """Cumprimenta o usuário pelo nome"""
#     # path = Path('.\\cap10\\username.json')
#     # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
      # path = Path(__file__).parent/'username.json'
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name: ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
# greet_user()

print('\nPrograma-05')
def get_stored_username(path):
    """Obtém o nome de usuário armazenado , se disponível"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Solicita um novo nome de usuário"""
    username = input("What is your name: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Cumprimenta o usuário pelo nome"""
    # path = Path('.\\cap10\\username.json')
    # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
    path = Path(__file__).parent/'username.json'
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
