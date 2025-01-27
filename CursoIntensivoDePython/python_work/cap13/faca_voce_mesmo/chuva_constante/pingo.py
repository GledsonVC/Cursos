import pygame
from pygame.sprite import Sprite

class Pingo(Sprite):
    """Classe para representar um pingo"""

    def __init__(self, pc):
        """Inicia os pingos e define posição inicial"""
        super().__init__()
        self.screen = pc.screen
        self.settings = pc.settings

        # Carrega imagem da gota
        self.image = pygame.image.load('images/gota.png')
        self.rect = self.image.get_rect()

        # Inicia cada alienígena novo perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alienígena
        self.y = float(self.rect.y)
    
    def check_disappeared(self):
        """Checa se o pinto está no fim da tela"""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move a gota para baixo"""
        self.y += self.settings.pingo_speed
        self.rect.y = self.y