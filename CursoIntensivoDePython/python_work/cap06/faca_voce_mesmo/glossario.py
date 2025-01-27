glossario = {
    'dicionario': 'Em Python é uma coleção de pares chaves-valor.',
    '.get()': 'Metodo ".get()" a fim de definirmos um valor padrão que será retornado se a chave solicitada não existir.',
    'del': 'Instrução "del"  pode ser utilizada com dicionário para remover completamento um par chave-valor.',
    'lista': 'Coleção de itens em uma ordem específica que podem ser modificadas.',
    'tupla': 'Identico a uma "lista", porem com itens imutáveis ou seja não podem ser modificadas.',
    }

chave_inexistente = glossario.get('chave_inexistente', 'Não existe a chave no dicionário glossario "chave_inexistente".')
print(f"\n{chave_inexistente}")

chave = 'dicionario'
print(f"\n{chave.title()}: \n\t{glossario[chave]}")

chave = '.get()'
print(f"\n{chave}: \n\t{glossario[chave]}")

chave = 'del'
print(f"\n{chave.title()}: \n\t{glossario[chave]}")

chave = 'lista'
print(f"\n{chave.title()}: \n\t{glossario[chave]}")

chave = 'tupla'
print(f"\n{chave.title()}: \n\t{glossario[chave]}")
