import pygame
from pygame.sprite import Sprite

class Estrela(Sprite):
    """Inicia a classe que representa a estrela"""

    def __init__(self, estrela_jogo):
        super().__init__()
        self.screen = estrela_jogo.screen


        # Pega a imagem da estrela e atribui a reação
        self.image = pygame.image.load('images/estrela.png')
        self.rect = self.image.get_rect()

        # Inicia a posição da estrela na tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


