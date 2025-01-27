pessoas = ['ellen' , 'luan', 'zoraide', 'maria']
print(f'Vamos a um restaurante {pessoas[0].title()}?')
print(f'Vamos a um restaurante {pessoas[1].title()}?')
print(f'Vamos a um restaurante {pessoas[2].title()}?')
print(f'Vamos a um restaurante {pessoas[-1].title()}?')

#pessoa que não vai poder ir e incluindo outra pessoa
print(f'Que pena que {pessoas[2].title()} não poderá comparecer no restaurante')
pessoas[2] = 'clovis'
print(f'Vamos a um restaurante {pessoas[2].title()}?')
