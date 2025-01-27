favorite_places = {
    'gledson' : ['praia', 'cachoeira', 'sítio'],
    'ellen' : ['praia', 'restaurante', 'sítio'],
    'luan' : ['praia', 'piscína', 'restaurante'],
}
for nome in favorite_places.keys():
    print(f"{nome.title()} gosta de ir para:")
    for lugar in favorite_places[nome]:
        print(f"\t{lugar}")
