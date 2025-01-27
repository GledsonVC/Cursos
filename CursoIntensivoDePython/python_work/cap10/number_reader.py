from pathlib import Path
import json

# path = Path('.\\cap10\\numbers.json')
# # Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'numbers.json'
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
