numeros = {
    'gledson': [21, 5], 
    'ellen': [10, 31, 2017, 1987], 
    'luan': [10, 11, 12], 
    }
for nome, numeros_favoritos in numeros.items():
    print(f"{nome.title()} gosta dos números:")
    for numero in numeros_favoritos:
        print(f"\t{numero}")
