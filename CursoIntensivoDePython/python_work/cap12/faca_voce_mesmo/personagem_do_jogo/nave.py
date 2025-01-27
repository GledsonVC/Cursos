import pygame


class Nave:
    """Classe para cuidar da espaçonave"""


    def __init__(self, nave_alienigena):
        """Inicia a espaçonave e defina sua posição inicial"""
        self.screen = nave_alienigena.screen
        self.screen_rect = nave_alienigena.screen.get_rect()

        # Sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/nave.bmp')
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom
    

    def carregue_me(self):
        """Desenha a nave em sua localização atual"""
        self.screen.blit(self.image, self.rect)


