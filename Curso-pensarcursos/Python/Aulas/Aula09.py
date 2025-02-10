import random
 
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
palavras = 'banana telescópio cachorro martelo girafa hamburger chocolate alimentos biscoito carne supermercado  tia tio pai mae'.split()
 
def main():
    """
    Função Principal do programa
    """
    global FORCAIMG
    print('F O R C A')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True
    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        palpite = recebePalpite(letrasErradas + letrasAcertadas)
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é " +palavraSecreta+'!Você ganhou!!')
                jogando = False
        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG)-1:
               imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
               print("Você excedeu o seu limite de palpites!")
               print("Depois de "+str(len(letrasErradas))+' letras erradas e '+str(len(letrasAcertadas)), end = ' ')
               print("letras corretas, a palavra era "+palavraSecreta+'.')
               jogando = False
        if not jogando:
            if JogarNovamente():
               letrasErradas = ''
               letrasAcertadas = ''
               jogando = True
               palavraSecreta = geraPalavraAleatória().upper()

def geraPalavraAleatória():
    """
    Função que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras) # .random -> para sortear, .choice(palavra) -> para pegar apenas a variavel global sem o espaço

def imprimeComEspacos(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaço entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end = '')
    print()

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    """
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)] + '\n')

    print("Letras Erradas: ", end = ' ')
    imprimeComEspacos(letrasErradas)

    vazio = '_'*len(palavraSecreta)

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
       
    imprimeComEspacos(vazio)

def recebePalpite(palpitesFeitos):
    """
    Função feita para garantir que o usuário coloque uma
    entrada válida, ou seja, que seja uma única letra
    que ele ainda não tenha chutado
    """
    while True:
        print()
        palpite = input("Advinhe uma letra. \n").upper() # .upper() -> convertendo em letra maiuscula a letra que digitar
        if len(palpite) != 1:
            print("Coloque uma única letra.")
        elif palpite in palpitesFeitos:
            print("Esta letra já existe, digite outra.")
        elif not 'A' <= palpite <= 'Z':
            print("Insira apenas letras.")
        else:
            return palpite

def JogarNovamente():
    """
    Função que pede para o usuário decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input("Você quer jogar novamente? (Sim ou Não) \n").upper().startswith('S') # startswith -> consegue verificar e capturar a primeira letra digitada
    

     
def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    """
    Função que verifica se o usuário acertou todas as
    letras da palavra secreta
    """
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main()     
