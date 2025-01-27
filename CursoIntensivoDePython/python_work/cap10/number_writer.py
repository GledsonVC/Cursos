from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
# path = Path('numbers.json')
# # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'numbers.json'
contents = json.dumps(numbers)
path.write_text(contents)
