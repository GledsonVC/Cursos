from pathlib import Path

print('\nPrograma-01')
# path = Path('.\cap10\lendo_arquivo\pi_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text()
print(contents)

print('\nPrograma-02')
# path = Path('.\cap10\lendo_arquivo\pi_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text()
contents = contents.rstrip()
print(contents)

print('\nPrograma-02.1')
# path = Path('.\cap10\lendo_arquivo\pi_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text().rstrip()
print(contents)

print('\nPrograma-03')
# path = Path('.\cap10\lendo_arquivo\pi_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
