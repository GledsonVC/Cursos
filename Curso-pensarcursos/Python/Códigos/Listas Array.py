"""cesta = ["Banana", "Maça", "Laranja", ["Uva", "Pera"] ]

#for i in range(3):
print(cesta[3][0])

print(len(cesta))
"""



lista = []
num = int(input("Digite um valor: "))

while num != -1:
   lista.append(num) 
   num = int(input("Digite um valor: "))

elemento = int(input("Qual o valor a ser procurado: "))

cont = 0

for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1

print("O elemento %i aparece %i vezes na sequencia." %(elemento, cont))

