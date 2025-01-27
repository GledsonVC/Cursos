from city_function_pop import cidade_pais


def test_city_country():
    """Cidade e país como 'Santiago, Chile' funcionam?"""
    formatado_cidade_pais = cidade_pais('santiago', 'chile')
    assert formatado_cidade_pais == 'Santiago, Chile'


def test_city_country_population():
    """
    Cidade, pais e população como 'Santiago, Chile - população 5000000', 
    funcionam?
    """
    formatado_cidade_pais_populacao = cidade_pais(
        'santiago', 'chile', populacao=5000000
    )
    afirmar = 'Santiago, Chile - population 5000000'
    assert formatado_cidade_pais_populacao == afirmar
