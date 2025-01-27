from pathlib import Path

# Solicita usuário o nome
nome = input('Escreva seu nome: ')

# Coloca o nome informado no arquivo guest.txt
path = Path(__file__).parent / 'guest.txt'
path.write_text(nome)
