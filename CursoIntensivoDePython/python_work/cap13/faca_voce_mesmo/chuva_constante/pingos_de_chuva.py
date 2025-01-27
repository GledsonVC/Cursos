import sys

import pygame

from settings import Settings
from pingo import Pingo

class PingosDeChuva:
    """Classe que cria a chuva"""

    def __init__(self):
        """Inicializa o a chuva"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Pingos de chuva")

        self.pingos = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        """Inicia o Loop principal"""
        while True:
            self._check_events()
            self._atualiza_pingos()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responde ações e teclas"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responde teclas pressionadas"""
        if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
            sys.exit()


    def _create_drops(self):
        """Cria chuva e pingos"""
        pingo = Pingo(self)
        pingo_width, pingo_height = pingo.rect.size

        current_x, current_y = pingo_width, pingo_height
        while current_y < (self.settings.screen_height - 2 * pingo_height):
            while current_x < (self.settings.screen_width - 2 * pingo_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * pingo_width

            # Finished a row; reset x value, and increment y value.
            current_x = pingo_width
            current_y += 2 * pingo_height

    def _create_drop(self, x_posicao, y_posicao):
        """Cria Chuva e atualiza o grid."""
        novo_pingo = Pingo(self)
        novo_pingo.y = y_posicao
        novo_pingo.rect.x = x_posicao
        novo_pingo.rect.y = y_posicao
        self.pingos.add(novo_pingo)
    
    def _create_new_row(self):
        """Cria novas chuvas depois do sisplay"""
        pingo = Pingo(self)
        pingo_width, pingo_height = pingo.rect.size

        current_x = pingo_width
        current_y = -1 * pingo_height
        while current_x < (self.settings.screen_width - 2 * pingo_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * pingo_width        
    

    def _atualiza_pingos(self):
        """Atualiza chuva"""
        self.pingos.update()

        # Assume we won't make new drops.
        fazer_novas_gotas = False
        for pingo in self.pingos.copy():
            if pingo.check_disappeared():
                # Remove os pingos e adciona no inicio da tela.
                self.pingos.remove(pingo)
                fazer_novas_gotas = True

        # Make a new row of drops if needed.
        if fazer_novas_gotas:
            self._create_new_row()

    def _update_screen(self):
        """Atualiza a tela e as imagens"""
        self.screen.fill(self.settings.bg_color)
        self.pingos.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Instancia o jogo e inicia.
    rd_game = PingosDeChuva()
    rd_game.run_game()
