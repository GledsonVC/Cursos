print(80 * '-')
print('\nPrograma-01')
def build_person(first_name, last_name):
    """Retorna um dicionário de informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
print(80 * '-')

print('\nPrograma-02')
def build_person(first_name, last_name, age=None):
    """Retorna um dicionário de informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
print(80 * '-')
