def describe_city(nome_cidade, pais='brasil'):
    '''função que retorna nome de cidade e pais'''
    print(f'\n {nome_cidade.title()} fica na(o) {pais.title()}')

# Chama a função apenas com o nome da cidade
describe_city('são paulo')

# Chamada de função usando argumentos nomeados invertido
describe_city(pais='estados unidos', nome_cidade='new york')

# Chamada de função só com o argumento nomeado da cidade
describe_city(nome_cidade='rio de janeiro')
