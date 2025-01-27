"""
Peça uma lista de números inteiros para o usuário
e imprima a lista sem repetições
"""


n = int(input("Digite o numero de elementos da lista: "))

lista = []
aux = []

for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: " %(i + 1,n)))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for ele in aux:
    aparicoes = lista.count(ele)
    for i in range(aparicoes-1):
        lista.remove(ele)
        
print(lista)


