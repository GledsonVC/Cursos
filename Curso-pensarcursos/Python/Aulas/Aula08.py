tamanho_max = 26

def recebeModo():
    """
    Função que pergunta se o usuário quer criptografar ou
    decriptografar e garante que uma entrada válida foi recebida
    """
    while True:
        modo = input("Você deseja criptograr ou descriptografar? \n").lower() # .lower() método para deixar em minusculoa
        if modo in 'criptografar c descriptografar d'.split(): # .split() método para separar palavras
            return modo
        else:
            print("Entre 'criptografar' ou 'c' ou 'descriptografar' ou 'd'.")

def recebeChave():
    """
    Função que pede o valor da chave para o usuário
    e devolve a chave caso o valor desta esteja adequado
    """
    global tamanho_max
    chave = 0
    while True:
        chave = int(input('Entre com o número da chave (1-%s)' %(tamanho_max)))
        if 1 <= chave <= tamanho_max:
            return chave
   
 
def geraMsgTraduzida(modo, mensagem, chave):
    """
    Traduz a mensagem do usuário de modo conveniente
    """
    if modo[0] == 'd':
        chave *= -1
    traduzido = ''
    for simbolo in mensagem:
        if simbolo.isalpha(): # isalpha() metodo para verificar se contem caracter especial
            num = ord(simbolo) # ord(X) função para ordenar 
            num += chave

            if simbolo.isupper():
                if num > ord('Z'): 
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduzido += chr(num) # chr(X) função para pegar o caracter
        else:
            traduzido += simbolo
    return traduzido


def main():
    """
    Função principal do programa
    """
    modo = recebeModo()
    mensagem = input("Entre com sua mensagem \n")
    chave = recebeChave()
    print("Seu texto traduzido é: ")
    print(geraMsgTraduzida(modo, mensagem, chave))

main()


"""
# Explicou como fazer para criar um arquivo ou ler o mesmo
arquivo = open('Hugo.txt', 'w')


# w - write   -Escrever
# r - read    -Ler
# a - append  -Extender


arquivo.close()
"""