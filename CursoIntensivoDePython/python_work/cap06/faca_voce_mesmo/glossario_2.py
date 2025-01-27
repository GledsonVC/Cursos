glossario = {
    'dicionario': 'Em Python é uma coleção de pares chaves-valor.',
    '.get()': 'Metodo ".get()" a fim de definirmos um valor padrão que será retornado se a chave solicitada não existir.',
    'del': 'Instrução "del"  pode ser utilizada com dicionário para remover completamento um par chave-valor.',
    'lista': 'Coleção de itens em uma ordem específica que podem ser modificadas.',
    'tupla': 'Identico a uma "lista", porem com itens imutáveis ou seja não podem ser modificadas.',
    'dicionario.items()': 'Método ".items()" utilizado para loop for para retornar chave e valor do dicionario.',
    'dicionario.key()': 'Método ".key()" para retornar apenas as chaves de um dicionario.',
    'sorted(dicionario.key())': 'Função "sorted()" que ordena as chaves do dicionario junto ao metodo ".key()".',
    'dicionario.values()': 'Método ".values()" para retornar apenas os valores de um dicionario.',
    'set(dicionario.values())':'Função "set()" que traz os valores não repetidos do dicionario junto ao metodo ".values()", muito utilizado quando contem valores identicos ao qual não quer que se repetem.',
    }
for chave, valor in glossario.items():
    print(f'\n{chave}: \n\t{valor}')
