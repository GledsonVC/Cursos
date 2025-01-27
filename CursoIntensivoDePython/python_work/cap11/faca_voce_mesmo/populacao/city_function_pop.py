def cidade_pais(cidade, pais, populacao=0):
    """
    Retorna string no formato 'Cidade, Pais' ou ''Cidade, Pais - population XXX
    '"""
    form_geral = f'{cidade.title()}, {pais.title()}'
    if populacao:
        form_geral += f' - population {populacao}'
    return form_geral
