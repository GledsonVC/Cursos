from pathlib import Path

print('\nPrograma-01')
# path = Path('.\cap10\lendo_arquivo\pi_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)
print(len(pi_string))

print('\nPrograma-02')
# path = Path('.\cap10\lendo_arquivo\pi_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_digits.txt'
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

print('\nPrograma-03')
# path = Path('.\cap10\lendo_arquivo\pi_million_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_million_digits.txt'
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))
