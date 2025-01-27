def show_mensagens(lista_de_mensagens):
    """Recebe uma lista de mensagens e exibe em tela formatada"""
    for mensagem in lista_de_mensagens:
        print(f'\n{mensagem}')

lista_mensagens = [
    'Água mole, pedra dura, tanto bate até que fura.', 
    'A pressa é a inimiga da perfeição.',
    'Papagaio que acompanha joão-de-barro vira ajudante de pedreiro.',
    ]
show_mensagens(lista_mensagens)
