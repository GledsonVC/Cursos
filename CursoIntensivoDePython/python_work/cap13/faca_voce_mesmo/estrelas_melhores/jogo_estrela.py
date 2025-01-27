import sys
import pygame

from settings import Settings
from estrela import Estrela
from random import randint

class JogoEstrela:
    """Classe geral para gerenciar ativos do compatamento do jogo"""

    def __init__(self):
        """Inicia o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_widht, self.settings.screen_height))
        pygame.display.set_caption("Estrelas")

        self.estrelas = pygame.sprite.Group()
        self._criar_estrelas()

    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._checar_eventos()            
            self._atualizar_tela()
            self.clock.tick(60)

    def _checar_eventos(self):
        """Responde envento de mouse e teclado"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checar_teclado_pressionado(event)
    

    def _checar_teclado_pressionado(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
    
    def _criar_estrelas(self):
        """Cria frota de estrelas"""
        estrela = Estrela(self)
        estrela_width, estrela_height = estrela.rect.size

        current_x, current_y = 2*estrela_width, 2*estrela_height
        while current_y < (self.settings.screen_height - 3 * estrela_height):
            while current_x < (self.settings.screen_widht - 2 * estrela_width):
                self._cria_estrela(current_x, current_y)
                current_x += 2 * estrela_width

            # Finished a row; reset x value, and increment y value.
            current_x = 2 * estrela_width
            current_y += 2 * estrela_height


    def _cria_estrela(self, x_posicao, y_posicao):
        """Cria estrela no tela"""
        nova_estrela = Estrela(self)
        nova_estrela.rect.x = x_posicao + self._desloca_estrela()
        nova_estrela.rect.y = y_posicao + self._desloca_estrela()
        self.estrelas.add(nova_estrela)
    
    def _desloca_estrela(self):
        """Retorna ponto deslocado para estrela"""
        desloca = 10
        return randint(desloca*-1, desloca)

    
    def _atualizar_tela(self):
        """Atualiza imagens na tela e flip da nova tela"""
        # Redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_collor)
        self.estrelas.draw(self.screen)

        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()




if __name__ == '__main__':
    je = JogoEstrela()
    je.run_game()