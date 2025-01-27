from pathlib import Path


path = Path(__file__).parent / 'guest_book.txt'

# pergunta para usuário do loop
pergunta = '\nOla, qual é seu nome? '
pergunta += "\nDigite 'sair' se voce for o ultimo convidado.\n"


# Loop para pegar a informação dos convidados e adcionar a uma lista de 
# convidados
convidados = []
while True:
    nome = input(pergunta)
    if nome == 'sair':
        break
    print(f'Obrigado {nome} adicionaremos você a lista de convidados.')
    convidados.append(nome)

# Transformando em uma string para passar para o arquivo
passar_arquivo = ''
for convidado in convidados:
    passar_arquivo += f'{convidado}\n'

path.write_text(passar_arquivo)
