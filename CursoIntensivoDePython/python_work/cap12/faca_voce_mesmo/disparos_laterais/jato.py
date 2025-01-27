import pygame

class Jato:
    """Classe para cuidar do jato"""

    def __init__(self, jt_game):
        """Inicia o jato e define sua posição"""
        self.screen =  jt_game.screen
        self.screen_rect = jt_game.screen.get_rect()
        self.configuracoes = jt_game.configuracoes
       

        # Sobe a imagem do jato e obtém seu rect
        self.image = pygame.image.load('images/jato.bmp')
        self.rect =self.image.get_rect()

        # Começa cada jato novo no centro do lado esquerdo da tela
        self.rect.centery = self.screen_rect.centery

        # Armazena um float para a posição vertical exata do jato
        self.y = float(self.rect.y)

        # Flag de movimento; começa com um jato que não está se movendo
        self.mover_cima = False
        self.mover_baixo = False

    
    def atualizar(self):
        """Atualiza a posição do jato com base nas flags de movimento"""
        # Atualiando o valor x do jato , não o rect
        if (self.mover_cima) and (self.rect.top > self.screen_rect.top):
            self.y -= self.configuracoes.velocidade_nave
        if (self.mover_baixo) and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.configuracoes.velocidade_nave
        
        # Atualiza o objeto react a partir de self.x
        self.rect.y = self.y

    
    
    def carregar(self):
        self.screen.blit(self.image, self.rect)
    
