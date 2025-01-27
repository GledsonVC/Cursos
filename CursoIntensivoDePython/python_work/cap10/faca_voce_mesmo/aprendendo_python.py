from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
conteudo = path.read_text()
print(conteudo)

linhas = conteudo.splitlines()
for linha in linhas:
    print(linha)
