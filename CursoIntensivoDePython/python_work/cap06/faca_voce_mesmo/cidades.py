cities = {
    'são paulo': {
        'country': 'brasil',
        'population': '12,33 milhões',
        'fact': 'Além de ser a cidade mais populosa do Brasil, São Paulo também está no pódio entre os municípios da América Latina no quesito número de habitantes. O Estado de São Paulo é considerado o maior em quantidade de estabelecimentos do Brasil, com mais de 75 mil restaurantes.',
    },
    'nova york': {
        'country': 'estados unidos',
        'population': '8,47 milhões',
        'fact': 'O Central Park(parque em Nova York) na verdade não é um parque natural. Ele foi construído de forma artificial a fim de adicionar mais natureza à cidade. Entretanto, isso não o diminui em nada, viu? Muito pelo contrário: seus 341 hectares contam com várias atrações e são sinônimos de lazer e tranquilidade',
    },
    'tóqui': {
        'country': 'japão',
        'population': '13,96 milhões',
        'fact': 'Tóquio é a capital do Japão e sede do governo nacional. É considerada uma das maiores metrópoles do planeta e também o centro político, econômico, educacional e cultural do Japão. A metrópole representa uma das áreas de maior aglomeração urbana do mundo. A metrópole é constituída por 23 bairros, 26 municípios adicionais e as ilhas Izu e Ogasawara.',
    },
}
for cidade, informacoes in cities.items():
    print(f"\nCidade de {cidade.title()}:")
    pais = informacoes['country']
    população = informacoes['population']
    curiosidade = informacoes['fact']
    print(f"\tPais: {pais.title()} ")
    print(f"\tPopulação: {população}")
    print(f"\tCuriosidade: {curiosidade}")
