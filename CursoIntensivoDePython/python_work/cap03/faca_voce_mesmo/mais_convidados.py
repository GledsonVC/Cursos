pessoas = ['ellen' , 'luan', 'zoraide', 'maria']
print(f'Vamos a um restaurante {pessoas[0].title()}?')
print(f'Vamos a um restaurante {pessoas[1].title()}?')
print(f'Vamos a um restaurante {pessoas[2].title()}?')
print(f'Vamos a um restaurante {pessoas[-1].title()}?')

#pessoa que não vai poder ir e incluindo outra pessoa
print(f'Que pena que {pessoas[2].title()} não poderá comparecer no restaurante')
pessoas[2] = 'clovis'
print(f'Vamos a um restaurante {pessoas[2].title()}?')

#Mensagem para todos que encontrei mesa maior
print(f'{pessoas[0].title()}, {pessoas[1].title()}, {pessoas[2].title()} e {pessoas[3].title()} encontrei uma mesa maior vou convidar mais 3 pessoas!')
pessoas.insert(0, 'diogo')
pessoas.insert(2, 'b2')
pessoas.append('pantoja')
print(f'Venho aqui convidar você {pessoas[0].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[1].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[2].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[3].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[-2].title()} a ir no restaurante.')
print(f'Venho aqui convidar você {pessoas[-1].title()} a ir no restaurante.')
