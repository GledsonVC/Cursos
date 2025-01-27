from pathlib import Path
import json

def armazena_numero(caminho):
    """Armazena número no local desejado"""
    numero_favorito = input('\nDigite um número: ')
    conteudo = json.dumps(numero_favorito)
    caminho.write_text(conteudo)
    return numero_favorito
    
caminho = Path(__file__).parent / 'numero_favorito.json'
numero_favorito = armazena_numero(caminho)
print(f'Lembraremos do seu número favorito: {numero_favorito}.\n')
