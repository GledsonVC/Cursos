from pathlib import Path
import json

# path = Path('.\\cap10\\username.json')
# Maneira que funciona tanto Windows quanto Linux pegando a raiz do arquivo
path = Path(__file__).parent / 'username.json'
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
