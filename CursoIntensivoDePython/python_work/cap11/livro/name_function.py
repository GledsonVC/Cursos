# def get_formatted_name(first, last): -> modificado para dar erro na chamada
# def get_formatted_name(first, middle, last): ->modificado para acerto teste
def get_formatted_name(first, last, middle=''):
    """Gera um nome completo, elegantemente formatado"""
    # full_name = f"{first} {last}"
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
