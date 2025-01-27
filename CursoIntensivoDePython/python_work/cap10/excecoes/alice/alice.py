from pathlib import Path

# path = Path('.\\cap10\\excecoes\\alice\\alice.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'alice.txt'
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Conta o número aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
