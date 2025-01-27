import sys
import pygame

from configuracoes import Configuracoes
from jato import Jato
from municao import Municao


class DisparoLaterais:
    """Classe para gerenciar comportamento do jogo"""

    def __init__(self):
        """Inicia o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.configuracoes = Configuracoes()
        self.screen = pygame.display.set_mode(
            (self.configuracoes.tela_largura, self.configuracoes.tela_altura))
        pygame.display.set_caption("Disparo Laterais")
        self.jato = Jato(self)
        self.bullets = pygame.sprite.Group()
    

    def rodar_jogo(self):
        while True:
            self._checar_eventos()
            self.jato.atualizar()
            self._atualizar_municoes()
            self._atualizar_tela()
            self.clock.tick(60)
    

    def _checar_eventos(self):
        """Responde as teclas pressionadas e eventos de mouse"""
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checar_tecla_pressionada(event)
            elif event.type == pygame.KEYUP:
                self._checar_tecla_solta(event)
    
    
    def _checar_tecla_pressionada(self, event):
        """Responde a teclas pressionadas"""
        # Se jogador pressionar Q irá finalizar o jogo
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.jato.mover_cima = True
        elif event.key == pygame.K_DOWN:
            self.jato.mover_baixo = True
        elif event.key == pygame.K_SPACE:
            self._atira_municao()

    
    def _checar_tecla_solta(self, event):
        """Responde a teclas soltas"""
        if event.key == pygame.K_UP:
            self.jato.mover_cima = False
        elif event.key == pygame.K_DOWN:
            self.jato.mover_baixo = False
    

    def _atira_municao(self):
        """Cria um novo projétil e o adciona ao grupo projéteis"""
        if len(self.bullets) < self.configuracoes.municao_permitida:
            new_bullet = Municao(self)
            self.bullets.add(new_bullet)
    

    def _atualizar_municoes(self):
        """Atualiza a posição dos projéteis e descarta projéteis antigos"""
        # Atualiza as posições dos projéteis
        self.bullets.update()

        # Descarta os projéteis que desaparecem
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)


    def _atualizar_tela(self):
        """Atualiza as imagens na tela e muda para a nova tela"""
        self.screen.fill(self.configuracoes.cor_de_fundo)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()       
        self.jato.carregar()
        pygame.display.flip()


if __name__ == '__main__':
    # Cria uma instancia do jogo e executa jogo
    jt = DisparoLaterais()
    jt.rodar_jogo()

