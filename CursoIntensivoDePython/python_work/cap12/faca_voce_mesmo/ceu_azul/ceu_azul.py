import sys
import pygame

from configuracao import Configuracao

class CeuAzul:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        self.cronometro = pygame.time.Clock()
        self.configuracao = Configuracao()
        
        # Tela
        self.tela = pygame.display.set_mode(
            (self.configuracao.largura_tela, self.configuracao.autura_tela)
        )
        pygame.display.set_caption("Céu azul")


    def rodar_tela(self):
        """Inicia o loop principal do do jogo"""
        while True:
            self._verificar_eventos()
            self._atualizacao_da_tela()
            self.cronometro.tick(60)
    
    
    def _verificar_eventos(self):
        """Responde as teclas pressionadas e a eventos de mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    

    def _atualizacao_da_tela(self):
        """Atualiza as imagens na tela e mude para a nova tela"""
        self.tela.fill(self.configuracao.cor_do_fundo_tela)
        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instancia do jogo e execute o jogo
    ca = CeuAzul()
    ca.rodar_tela()
