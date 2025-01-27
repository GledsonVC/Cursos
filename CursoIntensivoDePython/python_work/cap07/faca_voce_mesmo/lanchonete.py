sandwich_orders = ['hot-dog', 'x-calabresa',
                   'x-tudo', 'x-bacon', 'carne louca']
finished_sandwiches = []

# passar os sandwichws para a outra lista
# e exibindo mensagem Seu lanche X está pronto
print('\nPreparando lanches:')
while sandwich_orders:
    sanduiche = sandwich_orders.pop()
    print(f'Seu lanche de {sanduiche} está pronto.')
    finished_sandwiches.append(sanduiche)

# Exibe mensagem dos sanduiches numerando
# numero = 1
print('\nFinal do pedido \nID: lanche')
chave = 0
for chave in range(len(finished_sandwiches)):
    print(f'{chave+1} : {finished_sandwiches[chave]}')
