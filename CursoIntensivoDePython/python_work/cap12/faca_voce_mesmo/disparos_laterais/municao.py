import pygame
from pygame.sprite import Sprite


class Municao(Sprite):
    """Classe para gerenciar os projéteis disparados da espaçonave"""

    def __init__(self, jt_game):
        """Cria um objeto bullet na posição atual da espaçonave"""
        super().__init__()
        self.screen = jt_game.screen
        self.configuracoes = jt_game.configuracoes
        self.color = self.configuracoes.municao_cor

        # Cria um bullet rect em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(
            0, 0, self.configuracoes.municao_largura, 
            self.configuracoes.municao_altura
        )
        self.rect.midright = jt_game.jato.rect.midright

        # Armazena a posição do projétil com um float
        self.x = float(self.rect.x)
    

    def update(self):
        """Desloca o projétil verticalmente pela tela"""
        # Atualiza a posição exata do projétil
        self.x += self.configuracoes.municao_velocidade
        # Atualiza a posição do react
        self.rect.x = self.x


    def draw_bullet(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)

        
