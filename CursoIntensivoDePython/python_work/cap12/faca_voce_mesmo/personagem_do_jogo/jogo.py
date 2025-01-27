import sys
import pygame

from configuracao import Configuracao
from nave import Nave

class Jogo:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicia Jogo"""
        pygame.init()
        self.tempo = pygame.time.Clock()
        self.configuracao = Configuracao()
                


        self.screen = pygame.display.set_mode(
            (self.configuracao.largura_tela, self.configuracao.altura_tela))
        pygame.display.set_caption("Alien Invasion")

        self.nave = Nave(self)


    def roda_jogo(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._checar_eventos()
            self._atualizar_eventos()
            self.tempo.tick(60)
    
    
    def _checar_eventos(self):
        """Responde as teclas pressionadas e a eventos de mouse"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
    

    def _atualizar_eventos(self):
        """Atualiza as imagens na tela e mude para a nova tela"""
        self.screen.fill(self.configuracao.cor_fundo_tela)
        self.nave.carregue_me()

        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    jogo = Jogo()
    jogo.roda_jogo()
