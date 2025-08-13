def funcaoTupla(*tupla_variavel_lista_dicionario):
    return tupla_variavel_lista_dicionario


def funcaoDicionario(**dicionario_tupla_variavel_lista):
    return dicionario_tupla_variavel_lista


tupla = funcaoTupla('valor1', 'valor2') 

dicionario = funcaoDicionario(
    indice1 = 'valor1', 
    indice2 = 'valor2',
)

print(tupla)
print(dicionario)
