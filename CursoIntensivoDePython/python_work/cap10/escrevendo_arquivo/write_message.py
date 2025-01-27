from pathlib import Path


# path = Path('.\\cap10\\escrevendo_arquivo\\programming.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'programming.txt'
path.write_text("I love programming")
