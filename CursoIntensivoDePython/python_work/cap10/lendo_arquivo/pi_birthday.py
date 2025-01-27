from pathlib import Path

# path = Path('.\\cap10\\lendo_arquivo\\pi_million_digits.txt')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'pi_million_digits.txt'
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("You birthday appears in the first million digits of pi.")
else:
    print("You birthday does not appear in the first million digits of pi.")
