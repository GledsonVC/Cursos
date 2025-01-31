"""cesta = ["Banana", "Maça", "Laranja", "Pera"]

#for i in range(3):
print(cesta[3][1])

print(len(cesta))
"""

# lista = []
# num = int(input("Digite um valor: "))

# while num != -1:
#     lista.append(num)
#     num = int(input("Digite um valor: "))
    

# elemento = int(input("Qual o valor a ser procurado: "))

# cont = 0
# for i in range(len(lista)):
#     if lista[i] == elemento:
#         cont += 1
# print("O elemento %i aparece %i vezes na sequência."%(elemento, cont))


"""
Faça um programa que peça as quatro notas de 8 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 6.0
"""
# Feito por mim
alunos = []
# loop para atribuir 8 alunos
for aluno in range(0, 8):
    nota_aluno = 0
    # Loop para atribuit 4 notas do aluno
    for nota in range(0, 4):
        nota_aluno += float(input("Digite a %iª nota do %iª aluno: "%(nota+1, aluno+1)))
    alunos.append(nota_aluno / 4)
alunos_media_maior = 0
cont = 0
#Loop para contar a quantidade de alunos com médida >= 6
for aluno in alunos:
    if aluno >= 6:
        cont += 1
print("%i alunos que tiraram nota maior ou igual a 6.0 foram "%(cont))

