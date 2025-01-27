"""
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma conta ou fechar o programa. Se
ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que usuário selecione um número com 6 dígitos
e, então, se o número não existir no registro do banco, ele irá pedir um valor
de depósito. Depois o banco perguntara se se deseja ver o saldo do banco, se sim
ele deverá imprimir o balanço geral do banco, senão ele entrará em loop.
"""


contas = []
depositos = []
saldo = 0



def main():
    opcao = bool(int(input("Deseja ver ou criar a conta(1) ou fechar o programa(0): ")))
    while opcao:
        criarConta()
        verSaldo()
        opcao = bool(int(input("Deseja ver ou criar a conta(1) ou fechar o programa(0): ")))

def criarConta():
    global contas, depositos, saldo
    num_conta = int(input("Digite o numero da conta: "))

    while num_conta in contas:
        print("Conta já existente, Digite novamente.")
        num_conta = int(input("Digite o numero da conta: "))

    contas.append(num_conta)
    deposito = float(input("Digite o valor do primeiro deposito: "))
    while deposito <= 0:
        print("Valor do depósito invalido")
        deposito = float(input("Digite o valor do seu primeiro depósito: "))
    depositos.append(deposito)
    saldo += deposito

def verSaldo():
    global saldo
    opcao = bool(int(input("Deseja ver o saldo do banco(1 - Sim / 0 - Não: ")))
    if opcao:
        print("O saldo do banco é R$", saldo)

main()
                 
    


        
