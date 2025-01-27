"""
def soma(num1, num2):
    
    total = num1 + num2
    return total

valores = soma(5,6)

print(valores)
"""

"""
Escreva uma função que recebe dois números e devolve a soma e
a multiplicação entre os dois

 
def operacao(num1, num2):
   #soma = num1 + num2
    return  num1 + num2, num1*num2
a, b = operacao(2,3)
print(a,b)

"""

"""
def soma(*lista):
    soma_num = 0
    print(lista)

    for num in lista:
        soma_num += num

    return soma_num

a = (1,2,3,4)
print(soma(1,2,3,4,5))
"""

x = 10

def incrementa():
    global x
    incremento = 5
    x += incremento

incrementa()
print(x)







