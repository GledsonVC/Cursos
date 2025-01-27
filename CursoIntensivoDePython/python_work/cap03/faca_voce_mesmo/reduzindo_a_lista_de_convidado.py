pessoas = ['ellen' , 'luan', 'zoraide', 'maria']
print(f'Vamos a um restaurante {pessoas[0].title()}?')
print(f'Vamos a um restaurante {pessoas[1].title()}?')
print(f'Vamos a um restaurante {pessoas[2].title()}?')
print(f'Vamos a um restaurante {pessoas[-1].title()}?')

#pessoa que não vai poder ir e incluindo outra pessoa
print(f'\nQue pena que {pessoas[2].title()} não poderá comparecer no restaurante')
pessoas[2] = 'clovis'
print(f'Vamos a um restaurante {pessoas[2].title()}?')

#Mensagem para todos que encontrei mesa maior
print(f'\n{pessoas[0].title()}, {pessoas[1].title()}, {pessoas[2].title()} e {pessoas[3].title()} encontrei uma mesa maior vou convidar mais 3 pessoas!')
pessoas.insert(0, 'diogo')
pessoas.insert(2, 'b2')
pessoas.append('pantoja')
print(f'Venho aqui convidar você {pessoas[0].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[1].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[2].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[3].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[-2].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[-1].title()} a ir no restaurante.')

#só será possivel 2 pessoas na mesa para ser convidado
print('\n\tSó irei poder convidar 2 pessoas para o restaurante, pois só foi \nreservado uma mesa para duas pessoas no restaurante')
print(pessoas)
remove_pessoa = pessoas.pop(0)
print(f'Lamento por não poder te incluir a mesa no restaurante {remove_pessoa.title()}.')
remove_pessoa = pessoas.pop(1)
print(f'Lamento por não poder te incluir a mesa no restaurante {remove_pessoa.title()}.')
remove_pessoa = pessoas.pop()
print(f'Lamento por não poder te incluir a mesa no restaurante {remove_pessoa.title()}.')
remove_pessoa = pessoas.pop(-2)
print(f'Lamento por não poder te incluir a mesa no restaurante {remove_pessoa.title()}.')
remove_pessoa = pessoas.pop(-1)
print(f'Lamento por não poder te incluir a mesa no restaurante {remove_pessoa.title()}.')
print(f'\n{pessoas[0].title()} e {pessoas[1].title()} vcs ainda estão convidadas para ir ao restaurante')
#deletando as duas pessoas da lista
del pessoas[1]
del pessoas[0]
print(pessoas)
