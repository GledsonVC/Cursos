from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
contents = path.read_text()
print(contents)
for line in contents.splitlines():
    print(line)

imprime_linha = ''
for linha in contents.splitlines():
    imprime_linha += linha.replace('Python', 'C') + '\n'
print(imprime_linha)
