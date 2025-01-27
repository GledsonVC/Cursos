def city_country(nome_cidade, pais_da_cidade='brasil'):
    """Recebe nome de cidade e pais e retorna formatado"""
    formata_cidade_pais = f'{nome_cidade}, {pais_da_cidade}'
    return formata_cidade_pais.title()
# Chamada de 3 cidades e seus paises
cidade1 = city_country('são paulo', 'brasil')
print(cidade1)
cidade2 = city_country(pais_da_cidade='estados unidos', nome_cidade='new york')
print(cidade2)
cidade3 = city_country('rio de janeiro')
print(cidade3)
