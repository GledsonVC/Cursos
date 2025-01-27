from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data."

# path = Path('.\\cap10\\escrevendo_arquivo\\programming.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'programming.txt'
path.write_text(contents)
