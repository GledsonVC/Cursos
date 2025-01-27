print(80 * '-')
print('\nPrograma-1')
def get_formatted_name(first_name, last_name):
    """Retorna um nome completo, elegantemente formatado"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print(80 * '-')

print('\nPrograma-2')
def get_formatted_name(first_name, middle_name, last_name):
    """Retorna um nome completo, elegantemente formatado"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jhohn', 'lee', 'hooker')
print(musician)
print(80 * '-')

print('\nPrograma-3')
def get_formatted_name(first_name, last_name, middle_name=''):
    """Retorna um nome completo, elegantemente formatado"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jhohn', 'lee', 'hooker')
print(musician)
print(80 * '-')
