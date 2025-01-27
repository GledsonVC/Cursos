from pathlib import Path
import json


caminho = Path(__file__).parent / 'numero_favorito.json'

try:
    conteudo = caminho.read_text()
except FileNotFoundError:
    numero_favorito = input('\nDigite um número: ')
    conteudo = json.dumps(numero_favorito)
    caminho.write_text(conteudo)
    print(f'Lembraremos do seu número favorito: {numero_favorito}.\n')
else:
    numero_favorito = json.loads(conteudo)
    print(f'\nEu sei o seu número favorito! É {numero_favorito}.\n')
