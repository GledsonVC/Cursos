# Conversão para inteiro usar método int()

idade = int(input("Digite sua idade: "))
print("Eu tenho",  idade, "anos")


# Sistema de cálculos
x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))


print("A soma de", x, "+", y, "é", x + y)
print("A subtração de", x, "-", y, "é", x - y)
print("A multiplicação de", x, "x", y, "é", x * y)
print("A divisão de", x, "/", y, "é", x / y)

# Condicional
idade = int(input("Digite sua idade: "))
resp = idade >= 18
if resp == True:
    print("Tem idade para dirigir")
