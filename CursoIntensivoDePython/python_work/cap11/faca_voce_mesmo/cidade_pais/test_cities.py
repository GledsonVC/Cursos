from city_function import cidade_pais


def test_city_country():
    """Cidade e país como 'Santiago, Chile.' funcionam?"""
    formatado_cidade_pais = cidade_pais('santiago', 'chile')
    assert formatado_cidade_pais == 'Santiago, Chile'

