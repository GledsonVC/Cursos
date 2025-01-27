from pathlib import Path
import json


def obter_informacoes_do_usuario(caminho):
    """Obtém o nome de usuário armazenado , se disponível"""
    if caminho.exists():
        conteudo = caminho.read_text()
        dicionario_usuario = json.loads(conteudo)
        return dicionario_usuario
    else:
        return None

def novas_informacoes_de_usuario(caminho):
    """Solicita um novo nome, jogo, animal preferido de usuário"""
    nome_usuario = input('Qual é seu nome: ')
    jogo_usuario = input('Qual seu jogo favorito: ')
    animal_usuario = input('Qual seu animal favorito: ')
    dicionario_usuario = {
        'nome_usuario' : nome_usuario,
        'jogo_usuario' : jogo_usuario,
        'animal_usuario' : animal_usuario,
    }
    conteudo = json.dumps(dicionario_usuario)
    caminho.write_text(conteudo)
    return dicionario_usuario


def saudar_usuario():
    """Cumprimenta o usuário pelo nome"""
    caminho = Path(__file__).parent / 'dicionario_do_usuario.json'
    dicionario_usuario = obter_informacoes_do_usuario(caminho)
    if dicionario_usuario:
        print(f'Bem vindo, {dicionario_usuario["nome_usuario"].title()}!')
        print(
            'Espero que você esteja jogando ' + 
            dicionario_usuario['jogo_usuario'] + '!'
            )
        print(
            'Você viu um ' +
            dicionario_usuario['animal_usuario'] + ' recentemente?'
            )
    else:
        dicionario_usuario = novas_informacoes_de_usuario(caminho)
        print(dicionario_usuario['nome_usuario'].capitalize())
        print(f"Nos lembraremos de você quando você voltar!")

saudar_usuario()
