print(80 * '-')
print('\nPrograma-01')
def describe_pet(animal_type, pet_name):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
print(80 * '-')

print('\nPrograma-02')
def describe_pet(animal_type, pet_name):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
print(80 * '-')

print('\nPrograma-03')
def describe_pet(animal_type, pet_name):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')
print(80 * '-')

print('\nPrograma-04')
def describe_pet(animal_type, pet_name):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
print(80 * '-')

print('\nPrograma-05.1')
def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
print(80 * '-')

print('\nPrograma-05.2')
def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')
print(80 * '-')

print('\nPrograma-05.3')
def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='harry', animal_type='hamster')
print(80 * '-')

print('\nPrograma-05.4')
def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# Um cachorro chamado Willie
describe_pet('willei')
describe_pet(pet_name='willie')
# Um hamster chamado Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
print(80 * '-')

# Erro para na chamara da função com parâmetro destacado sem argumento
print('\nPrograma-6')
def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()
print(80 * '-')
