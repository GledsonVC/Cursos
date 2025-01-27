from pathlib import Path

# path = Path('.\\cap10\\excecoes\\alice.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'alice.txt'
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
