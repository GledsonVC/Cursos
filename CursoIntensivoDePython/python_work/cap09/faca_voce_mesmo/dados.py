from random import randint


class Die:
    """Criando dados"""

    def __init__(self, sides=6):
        self.sides = sides


    def roll_die(self, jogada=1):
        """Imprime na tela jogadas com quantidades estabelecidas"""
        mensagem = f'Lançando o dado de {self.sides} lados {jogada} vezes.'
        print('\n'+mensagem)
        lance = 1
        # loop para quantidade de jogadas e imprimindo
        while jogada != 0:
            print(f'Jogada({lance}): Dado deu {randint(1, self.sides)}')
            jogada -= 1
            lance += 1

# Criando dado com 6 lados
dado6 = Die()
dado6.roll_die(10)

# Criando dado com 10 lados
dado10 = Die(10)
dado10.roll_die(10)


# Criando dado com 20 lados
dado20 = Die(20)
dado20.roll_die(10)
