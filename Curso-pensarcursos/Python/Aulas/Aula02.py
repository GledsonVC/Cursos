# Condicional
idade = int(input("Digite sua idade: "))
"""
if idade >= 18:
    print("Tem idade para dirigir")
if idade < 18:
    print("Você não pode dirigir")
"""
# simplificando codigo acima
if idade >= 18:
    print("Tem idade para dirigir")
else:
    print("Você não pode dirigir")

# Criar um sistema que verifica qual o maior numero entre dois números inseridos
# e exiba na tela
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 == num2:
    print("Numeros iguais")
elif num1 > num2:
    print(num1, ">", num2)
else:
    print(num1, "<", num2)

# if elif alinhado
semana = int(input("Digite um número qualquer: "))

if semana == 1:
    print("Domingo")
elif semana == 2:
    print("Segunda")
elif semana == 3:
    print("Terça")
elif semana == 4:
    print("Quarta")
elif semana == 5:
    print("Quinta")
elif semana == 6:
    print("Sexta")
elif semana == 7:
    print("sabado")
else:
    print("Número inválido")

# Laço while
n = 10
cont = 0
while cont < n:
    print(cont)
    cont += 1

# Laço for
n = 10
cont = 0
for cont in range(n):
    print(cont)
