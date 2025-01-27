import pygame

class Nave:
    """Classe para cuidar da nave"""

    def __init__(self, es_game):
        """Inicia a nave e defina sua posição inicial"""
        self.screen = es_game.screen
        self.screen_rect = es_game.screen.get_rect()
        self.configuracoes = es_game.configuracoes
            
        # Sobe a imagem da nave e obtém seu rect
        self.image = pygame.image.load('images/nave.bmp')
        self.rect = self.image.get_rect()
        
        # Começa cada espaçonave nova no centro da tela
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Flag de movimento; começa com uma nave que não está se movendo
        self.mover_direita = False
        self.mover_esquerda = False
        self.mover_cima = False
        self.mover_baixo = False
    

    def atualizar(self):
        """Atualiza a posição da nave com base na flag de movimento"""
        # Atualiza o valor x da nave, não o rect
        if (self.mover_direita) and (self.rect.right < self.screen_rect.right):
            self.x += self.configuracoes.velocidade_nave
        if (self.mover_esquerda) and (self.rect.left > self.screen_rect.left): 
            self.x -= self.configuracoes.velocidade_nave
        if (self.mover_cima) and (self.rect.top > self.screen_rect.top):
            self.y -= self.configuracoes.velocidade_nave
        if (self.mover_baixo) and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.configuracoes.velocidade_nave
        
        # Atualiza o objeto react a partir de self.x
        self.rect.x = self.x
        self.rect.y = self.y
    
    
    def carregame(self):
        """Desenha a nave em sua localização atual"""
        self.screen.blit(self.image, self.rect)

