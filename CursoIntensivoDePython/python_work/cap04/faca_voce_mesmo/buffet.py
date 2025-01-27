pratos = ('bife', 'file de frango', 'calabresa defumada', 'a parmegiana', 'file de peixe')
print('Refeições que o restaurante oferece são:')
for prato in pratos:
    print(prato.title())

# erro de proposito no exercicio comentada
# pratos[0] = 'bife amilanesa'

pratos = ('bife à cavalo', 'file de frango empanado', 'calabresa defumada', 'parmegiana', 'file de peixe')
print('\nRestaurante mudou o cardápio estando agora com os pratos:')
for prato in pratos:
    print(prato.title())
