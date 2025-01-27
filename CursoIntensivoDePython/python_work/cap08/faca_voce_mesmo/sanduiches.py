def itens_lanche(*itens):
    print('\nPreparando sanduíche, itens:')
    for item in itens:
        print(f'- {item}')
itens_lanche('linguiça')
itens_lanche('linguiça', 'vinagrete')
itens_lanche('linguiça', 'vinagrete', 'azeitona')
