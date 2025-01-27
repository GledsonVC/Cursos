print(80 * '-')
print('\nPrograma-01')
def get_formatted_name(firs_name, last_name):
    """Retorna um nome completo, formatado elegantemente"""
    full_name = f"{firs_name} {last_name}"
    return full_name.title()
# Temos um loop infinito aqui!
# Comentado para continuar com o proximo programa
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")
print(80 * '-')

print(80 * '-')
print('\nPrograma-01')
def get_formatted_name(firs_name, last_name):
    """Retorna um nome completo, formatado elegantemente"""
    full_name = f"{firs_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
print(80 * '-')
