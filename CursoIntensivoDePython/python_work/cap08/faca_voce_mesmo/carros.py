def make_car(fabricante, modelo_do_carro, **carro):
    """Define um dicionário de um carro"""
    carro['fabricante'] = fabricante
    carro['modelo_do_carro'] = modelo_do_carro
    return carro

car = make_car(
    'subaru', 
    'outback', 
    color = 'blue',
    tow_package = True
    )
print(car)

for chave,valor in car.items():
    print(f'{chave}: {valor}')
