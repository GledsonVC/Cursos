import sys
import pygame

from configuracoes import Configuracoes

class Teclas:
    """Classe para criar uma Tela que responde o teclado"""

    def __init__(self):
        """Inicia tela"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.configuracoes = Configuracoes()
        self.screen = pygame.display.set_mode(
            (self.configuracoes.largura_tela, self.configuracoes.altura_tela)
        )
        pygame.display.set_caption("Teclas")
    

    def iniciar(self):
        """Executa programa"""
        while True:
            self._checar_eventos()
            self._atualiza_tela()
            self.clock.tick(60)
    
    def _checar_eventos(self):
        """Responde para teclado e mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checa_evento_teclado(event)
    

    def _checa_evento_teclado(self, event):
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()
    
    def _atualiza_tela(self):
        """Atualiza imagem na tela e atualiza nova tela """
        self.screen.fill(self.configuracoes.cor_fundo_tela)
        pygame.display.flip()
    

# inicia jogo
if __name__ == '__main__':
    t = Teclas()
    t.iniciar()
           
