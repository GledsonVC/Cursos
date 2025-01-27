print(80 * '-')
print('\nPrograma-01')
# Começa com alguns designs que precisam ser impressos.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simula a impressão de cada design, até que não reste nenhum
# Passa cada design para completed_models após impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Exibe todos os modelos comcluidos
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print(80 * '-')

print('\nPrograma-02')
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não reste nenhum
    Passa cada design para completed_models após impressão
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Exibe todos os modelos comcluidos"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(80 * '-')

print('\nPrograma-03')
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não reste nenhum
    Passa cada design para completed_models após impressão
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Exibe todos os modelos comcluidos"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Mesma coisa do programa 2 porem manda uma cópia da lista unprinted_desighns
# Podendo depois altera ela e não alterando a mesma na função print_models
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(80 * '-')
