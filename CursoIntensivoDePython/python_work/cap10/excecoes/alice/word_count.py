from pathlib import Path

def count_words(path):
    """ Conta o número aproximado de palavras em um arquivo"""
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Conta o número aproximado de palavrass no arquivo:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

print('\nPrograma-01')
# path = Path('alice.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'alice.txt'
count_words(path)

print('\nPrograma-02')
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']
for filename in filenames:
    path = Path(__file__).parent / filename
    count_words(path)

print('\nPrograma-03')
def count_words(path):
    """ Conta o número aproximado de palavras em um arquivo"""
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        pass
    else:
        # Conta o número aproximado de palavrass no arquivo:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']
# foi necessário criar o caminho relativo
caminho_relativo = '.\\cap10\\excecoes\\alice\\'
for filename in filenames:
    path = Path(__file__).parent / filename
    count_words(path)

    