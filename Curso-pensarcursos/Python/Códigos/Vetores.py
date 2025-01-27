"""
Faça um Programa que peça as quatro notas de 8 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 6.0.
"""

alunos = 8
medias = []

for i in range(1, alunos + 1):
    notas = 0
    for j in range(1 ,5):
        notas += float(input("Digite a nota %i de 4 notas do aluno %i de %i: " %(j, i, alunos)))
    notas /= 4
    medias.append(notas)


num = 0

for media in medias:
    if media >= 6:
        num += 1

print ("O numero de alunos com media maior que 6 é", num)       
    

        
