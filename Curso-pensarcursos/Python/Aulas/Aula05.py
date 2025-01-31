# """
# Faça um programa que peça as quatro notas de 8 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 6.0
# """
# alunos = 8
# medias = []

# for i in range(1, alunos+1):
#     notas = 0
#     for j in range(1,5):
#         notas += float(input("Digite a nota %i de 4 notas do aluno %i de %i: "%(j, i, alunos)))
#     notas /= 4
#     medias.append(notas)

# num = 0

# for media in medias:
#     if media >= 6:
#         num += 1

# print("O número de alunos com média maior que 6 é", num)

"""
Peça uma lista de números inteiros para o usuário
e imprima a lista sem repetições
"""
# # Feito por mim
# elemento_lista = int(input("Digite a quantidade de elemento de uma lista: "))
# lista = []
# lista_sem_repeti = []
# elemento = 0
# while elemento != elemento_lista:
#     numero = int(input("Digite o %iº numero de %i da lista: " %(elemento+1, elemento_lista)))
#     lista.append(numero)
#     if numero not in lista_sem_repeti:
#         lista_sem_repeti.append(numero)
#     elemento += 1
# print(lista) # caso queira ver a lista de números que foi criada repetindo
# print(lista_sem_repeti)

# n = int(input("Digite o número de elementos da lista: "))

# lista = []
# aux = []

# for i in range(n):
#     elemento = int(input("Digite o elemento %i de %i: " %(i + 1, n)))
#     lista.append(elemento)
#     aux.append(elemento)

# print(lista)

# for ele in aux:
#     aparicoes = lista.count(ele)
#     for i in range(aparicoes-1):
#         lista.remove(ele)

# print(lista)

# def soma(num1, num2):
#     total = num1 + num2
#     return total

# print(soma(4,5))
# valore = soma(5,6)
# print(valore)

"""
Escreva uma função que receba dois números e devolve a soma e 
a multiplicação entre os dois
# """
# # Eu fiz
# def funcao(num1, num2):
#     return(num1 + num2, num1 * num2)

# operacoes = funcao(2,3)
# print("A soma de 2 + 3 = %i" %(operacoes[0]))
# print("A multiplicação de 2 x 3 = %i" %(operacoes[1]))

"""
def operacao(num1, num2):
    # soma = num1 + num2
    return num1 + num2, num1 *num2

a, b = operacao(2,3)
print(a, b)
"""
"""
def soma(*lista):
    soma_num = 0
    print(lista)

    for num in lista:
        soma_num += num
    
    return soma_num

print(soma(1,2,3,4,5))
"""


"""
x = 10
def incrementa():
    global x
    incremento = 5
    x += incremento

incrementa()
print(x)
"""

"""
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma conta ou fechar o programa. Se
ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que usuário selecione um número com 6 dígitos
e, então, se o número não existir no registro do banco, ele irá pedir um valor
de depósito. Depois o banco pergunta se deseja ver o saldo do banco, se sim
ele deverá imprimir o balanço geral do banco, senão ele entrá em loop.
"""

# eu fiz

# Contas do banco
'''registro do banco'''
lista_contas = ['000001', '000002', '000003']

# Valor das contas seguindo indice das lista de contas
valor_contas = [100.00, 200.00, 300.00]


# Salda se não deseja criar a conta ou inicia o processo de criar conta 
def saldacao():
    '''O programa começa perguntando se o usuário quer criar uma conta'''
    if desejo_de_criar_conta():
        conta = criar_conta()
        if verifica_conta(conta):
            print(conta)
    else: 
        '''ou fechar o programa'''
        '''Se ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha'''
        print("Obrigado, volte sempre!")

# Retorna se deseja criar conta retornando True ou False (Boleano)
def desejo_de_criar_conta():
    '''O programa começa perguntando se o usuário quer criar uma conta'''
    cria_fecha = input("Deseja criar uma conta? [S]para sim ou [N]para não .Fechar o programa: ")[0]
    if cria_fecha in ('S', 's'):
        return True
    else:
        return False

# Cria conta de 6 digitos com 0.00 no valor da conta
def criar_conta():
    '''caso contrário ele vai pedir que usuário selecione um número com 6 dígitos'''
    numero = input("Digite um número de 6 digitos: ")[0:6] # pegando apenas os 6 digitos
    return numero

# se a conta já existe na lista de contas vai para deposito senão ele cria a conta com valor 0.00 e pergunta quanto será depositado
def verifica_conta(conta):
    # Declarando variavel globais
    global lista_contas, valor_contas
    '''e, então, se o número não existir no registro do banco,'''
    if conta in lista_contas:
        print(conta, "Conta existente no cadastro do banco.")
        '''ele irá pedir um valor de depósito'''
        depositar = input("Deseja fazer um deposito na conta? [S] Sim, [N] Não?: ")[0]
        if depositar in ('S','s'):
            deposito = float(input("Qual valor a ser depositado na conta? R$ "))
            deposito_conta(conta, deposito)
        else:
            saldacao()
    else:
        # Cria conta
        lista_contas.append(conta)
        # Ao criar a conta ele atribui já o valor de R$ 0.00
        valor_contas.append(0.00)
        print("Criando conta: ", conta)
        '''e, então, se o número não existir no registro do banco, ele irá pedir um valor de depósito.'''
        deposito_inicial = float(input("Qual valor de deposito na conta? R$ "))
        deposito_conta(lista_contas[-1], deposito_inicial)
        

# Acrescenta valor a conta 
def deposito_conta(conta, valor_a_deposito):
    # Declarando variavel globais
    global lista_contas, valor_contas
    indice_conta = 0
    # Varrendo para saber o indice da conta de todas as contas 
    while conta != lista_contas[indice_conta]:
        indice_conta += 1
    # Deposita o valor no indice da conta
    valor_contas[indice_conta] += valor_a_deposito
    '''
    Depois o banco pergunta se deseja ver o saldo do banco, se sim
    ele deverá imprimir o balanço geral do banco, senão ele entrá em loop.
    '''
    deseja_ver_saldo = 'N'
    while (deseja_ver_saldo != 'S') and (deseja_ver_saldo != 's'):
        deseja_ver_saldo = input("Deseja ver o saldo em conta? [S] Sim, [N] Não?: ")[0]
    verifica_saldo(indice_conta)

# Verificar o saldo
def verifica_saldo(indice_conta):
    # Declarando variavel globais
    global lista_contas, valor_contas
    print("Conta:",lista_contas[indice_conta], " Com saldo atual de R$ ", valor_contas[indice_conta])

# inicio do programa
saldacao()
