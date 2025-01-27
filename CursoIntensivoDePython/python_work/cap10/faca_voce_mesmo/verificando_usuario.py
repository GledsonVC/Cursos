from pathlib import Path
import json


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
    path = Path(__file__).parent / 'username.json'
    username = get_stored_username(path)
    if username:
        nome_verdadeiro = input(f'Você é {username.title()}? sim ou não (s/n)')
        nome_verdadeiro = nome_verdadeiro.lower()[0]
        if nome_verdadeiro == 's':
            print(f"Welcome back, {username.title()}!")
            return
    
    # Caso não tenha o aquivo ou usuário não for o mesmo 
    # irá chamar o novo usuário
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username.title()}!")


greet_user()
