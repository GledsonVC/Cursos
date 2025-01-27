class Settings:
    """Classe para armazenar as configurações do pingo de chuva"""

    def __init__(self):
        """Inicia as configurações de pingo de chuva"""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Configuração do pingo
        self.pingo_speed = 1.5