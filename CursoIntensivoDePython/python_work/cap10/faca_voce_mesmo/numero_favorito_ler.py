from pathlib import Path
import json

def ler_numero(caminho):
    """Verifica se a número registrado no local"""
    if caminho.exists():
        conteudo = caminho.read_text()
        numero_favorito = json.loads(conteudo)
        return numero_favorito
    else:
        return None
    
caminho = Path(__file__).parent / 'numero_favorito.json'
numero_favorito = ler_numero(caminho)
if numero_favorito:
    print(f'\nEu sei o seu número favorito! É {numero_favorito}.\n')
else:
    print(f'\nNumero não encontrado.\n')
