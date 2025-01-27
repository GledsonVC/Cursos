import sys
import pygame

from configuracoes import Configuracoes
from nave import Nave

class Espaconave:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        # Inicializa configurações de background de que Pygame precisa
        pygame.init()
        # Definindo relógio de frames por segundo
        self.clock = pygame.time.Clock()
        # instanciando Configuracoes com o nome configuracoes 
        self.configuracoes = Configuracoes()
        # Cria janela de exibição de acordo com a instancia configuracoes
        self.screen = pygame.display.set_mode(
            (self.configuracoes.largura, self.configuracoes.altura)
        )
        # Nome da janela
        pygame.display.set_caption("Espaçonave Pressione (Q) para sair")
        # instanciando Nave com nome nave
        self.nave = Nave(self)


    def run_game(self):
        """Inicia o loop principal do jogo"""
        # loop para observar eventos e ir atualizando a tela
        while True:
            # Chama a função que checa os eventos 
            self._checar_eventos()
            # chama a função de atualizar a nave
            self.nave.atualizar()
            # Chama a função que checa as atualizações 
            self._checar_atualizacao()            
            # Definindo o tempo em 60 fps(frames por segundo)
            self.clock.tick(60)
    

    def _checar_eventos(self):
        """Responde as teclas pressionadas e eventos de mouse"""
        # loop para bserva eventos de teclado e mouse do jogo
        for event in pygame.event.get():
            # Se jogador fechar a tela ele finaliza o jogo
            if event.type == pygame.QUIT:
                sys.exit()
            # Se movimentar a nave com as setas precionada
            elif event.type == pygame.KEYDOWN:
                self._checar_tecla_pressionada(event)
            # Para de movimentar a nave quando a seta não precionada
            elif event.type == pygame.KEYUP:
                self._checar_tecla_solta(event)


    def _checar_atualizacao(self):
        """Atualiza as imagens na tela e muda para a nova tela"""
        # Deixando a cor de fundo da tela do background de acordo com a 
        #    instancia configuracoes
        self.screen.fill(self.configuracoes.cor_de_fundo)
        # Carrega a nave da instancia Nave
        self.nave.carregame()
        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()
    

    def _checar_tecla_pressionada(self, event):
        """Responde a teclas pressionadas"""
        # Se jogador pressionar Q irá finalizar o jogo
        if event.key == pygame.K_q:
                sys.exit()
        # Verifica seta para a DIREITA
        elif event.key == pygame.K_RIGHT:
            # Move a nave para a DIREITA
            self.nave.mover_direita = True
        # Verifica seta para a ESQUERDA
        elif event.key == pygame.K_LEFT:
            # Move a nave para a ESQUERDA
            self.nave.mover_esquerda = True
        # Verifica seta para CIMA
        elif event.key == pygame.K_UP:
            # Move a nave para CIMA
            self.nave.mover_cima = True
        # Verifica seta para BAIXO
        elif event.key == pygame.K_DOWN:
            # Move a nave para BAIXO
            self.nave.mover_baixo = True

    
    def _checar_tecla_solta(self, event):
        """Responde a teclas soltas"""
        # Desliga quando para de precionar para DIREITA
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = False
        # Desliga quando para de precionar para ESQUERDA
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = False
        # Desliga quando para de precionar para CIMA
        elif event.key == pygame.K_UP:
            self.nave.mover_cima = False
        # Desliga quando para de precionar para BAIXO
        elif event.key == pygame.K_DOWN:
            self.nave.mover_baixo = False


# Inicio do programa
if __name__ == '__main__':
    # Cria uma instancia do jogo e executa o jogo
    es = Espaconave()
    es.run_game()

