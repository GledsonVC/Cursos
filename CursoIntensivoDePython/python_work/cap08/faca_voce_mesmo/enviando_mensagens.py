def show_mensagens(lista_de_mensagens):
    """Recebe uma lista de mensagens e exibe em tela formatada"""
    for mensagem in lista_de_mensagens:
        print(f'\n{mensagem}')

def send_mensagens(lista_1, sent_messages):
    """
    Recebe duas listas e imprime a medida que move para segunda lista:
        primeira lista com as mensagens
        segunda lista vazia
    """
    while lista_1:
        mensagem = lista_1.pop()
        print(f'\nMovendo mensagem para segunda lista: \n{mensagem}')
        sent_messages.append(mensagem)

# Criando as duas lista
# Lista cheia
lista1 = [
    'Água mole, pedra dura, tanto bate até que fura.', 
    'A pressa é a inimiga da perfeição.',
    'Papagaio que acompanha joão-de-barro vira ajudante de pedreiro.',
    ]
# Lista vazia
lista2 = []

# Chamando a função com as duas listas
send_mensagens(lista1, lista2)

# Mostrando a primeira lista para verificar se ficou vazia
print(lista1)
# Mostrando a segunda lista para verificar se está com conteúdo da lista1
print(lista2)
