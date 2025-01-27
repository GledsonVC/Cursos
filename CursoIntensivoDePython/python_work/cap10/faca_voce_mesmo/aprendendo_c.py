from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
conteudo = path.read_text()
linhas = conteudo.splitlines()
imprime_linha = ''
for linha in linhas:
    imprime_linha += linha.replace('Python', 'C') + '\n'
print(imprime_linha)
