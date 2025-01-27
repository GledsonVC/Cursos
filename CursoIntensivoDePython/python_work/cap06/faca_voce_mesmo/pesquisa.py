favorite_langages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
pessoas = ['gledson', 'phil', 'ellen', 'sarah', 'jen', 'luan', 'edward']
for pessoa in pessoas:
    if pessoa in favorite_langages.keys():
        print(f'Obrigado {pessoa.title()} por ter participado da enquete e dito que {favorite_langages[pessoa].title()} é a sua linguagem de programação preferida.')
    else:
        print(f'Olá {pessoa.title()}, gostaria de responder a enquete de linguagem preferida?')

for pessoa in pessoas:
    favorite_langages.get(print(f'Obrigado {pessoa.title()} por ter participado da enquete e dito que {favorite_langages[pessoa].title()} é a sua linguagem de programação preferida.'), print(f'Olá {pessoa.title()}, gostaria de responder a enquete de linguagem preferida?'))
