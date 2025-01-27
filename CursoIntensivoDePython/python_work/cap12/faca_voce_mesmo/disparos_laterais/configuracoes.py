class Configuracoes:
    """Classe para armazenar as configurações do jogo"""

    def __init__(self):
        """Inicia as configurações do jogo"""
        self.cor_de_fundo = (135,206,235)
        self.tela_largura = 1200
        self.tela_altura = 800
    
        # Configurações da nave
        self.velocidade_nave = 2
        
        # Configurações do projétil
        self.municao_velocidade = 2.0
        self.municao_largura = 15
        self.municao_altura = 3
        self.municao_cor = (60, 60, 60)
        self.municao_permitida = 10
