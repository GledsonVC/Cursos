sandwich_orders = [
    'hot-dog', 
    'pastrami',
    'x-calabresa',
    'pastrami',
    'x-tudo', 
    'pastrami',
    'x-bacon', 
    'carne louca',
]
finished_sandwiches = []

# Mensagem dizendo que não contem pastrami na lanchonete
print('A lanchonete está sem pastrame!')
# loop poara remover pastrami da lista de sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)

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
