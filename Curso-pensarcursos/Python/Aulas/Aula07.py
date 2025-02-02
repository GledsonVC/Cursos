# Explicação break
"""for i in range(10):
    if i == 5:
        break
    print(i)
"""

# Explicação continue
"""
for i in range(10):
    if i == 5:
        continue
    print(i)
"""

"""
Escreva uma função que produza a soma dos primeiros
n números de uma lista com tamanho m
"""
"""
def criaLista():
    lista = []
 
    m = int(input("Digite o tamanho da lista: "))
 
    for i in range(m):
        ele = float(input("Digite o elemento %i de %i: "%(i+1, m)))
        lista.append(ele)
 
    return lista
 
def main():
    l1 = criaLista()
 
    n = int(input("Digite o número de elementos que se deseja somar: "))
 
    soma = 0
    for i in range(len(l1)):
        if i == n:
            break
        soma += l1[i]
 
    print("A soma é", soma)
 
main()

"""

# Explicação de strings com print e seu retornos dependendo da variável
x = 1
print("o valor de X é %i" %(x))

nome  =  input("Digite seu nome: ")
x = "Ola %s, seja bem vindo ao nosso Curos" %(nome)
print(x)

# pessoal descoberta
flutuante = float(1.1151)
print("Numero com quantidade decimal é %f" %(flutuante))
