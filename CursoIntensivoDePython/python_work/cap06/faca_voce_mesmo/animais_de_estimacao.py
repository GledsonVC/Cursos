pets = []
animal = {
    'tipo de animal': 'cachorro',
    'nome': 'natasha',
    'dono': 'gledson',
    'alimento': 'ração de cachorro',
    'idade': '10',
}
pets.append(animal)
animal = {
    'tipo de animal': 'roedor',
    'nome': 'lua',   
    'dono': 'ellen',
    'alimento': 'ração em geral',
    'idade': 1,
}
pets.append(animal)
animal = {
    'tipo de animal': 'passaro',
    'nome': 'nego',
    'dono': 'luan',
    'alimento': 'ração de passaro preto',
    'idade': 11,
}
pets.append(animal)
for pet in pets:
    print(f"\nNOME DO PET: {pet['nome'].title()}")
    for chave, valor in pet.items():
        if chave in ('nome', 'dono'):
            print(f"\t{chave.upper()}: {valor.title()}")
        else:
            print(f"\t{chave.upper()}: {valor}")
