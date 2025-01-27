rios = {
    'tietê': 'brasil',
    'amazonas' : 'brasil',
    'nilo': 'egito',
}

# Loop para falar o nome do rio em que pais se localixa e uma observação dele
for rio, pais in rios.items():
    print('\n')
    if rio == 'tietê':
        print(f'Rio {rio.title()} localizado no {pais.title()}')
        print(
            '\tO rio Tietê é um curso de água do estado de São Paulo, sendo um afluente do rio Paraná. É conhecido nacionalmente por atravessar, ao longo de seus 1100 quilômetros de extensão, praticamente todo o estado de São Paulo, de leste a oeste, além de marcar a geografia urbana da maior cidade do país, São Paulo. O Tietê nasce no município de Salesópolis, a 22 km do oceano Atlântico, e corre para o interior de São Paulo, sendo assim, foi muito utilizado pelos índios e bandeirantes para acessar as vilas que se encontravam ao longo do rio.')
    elif rio == 'amazonas':
        print(f'Rio {rio.title()} localizado no {pais.title()}')
        print(
            '\tRio Amazonas (Brasil): possui 6 868 km de extensão, além disso, detém um grande volume de água, o que o torna o maior rio do mundo. O Amazonas nasce na Cordilheira dos Andes (Peru), recebe águas de diversos afluentes e desemboca no Oceano Atlântico, no litoral norte do Brasil.')
    elif rio == 'nilo':
        print(f'Rio {rio.title()} localizado no {pais.title()}')
        print(
            '\tRio Nilo (Egito): possui 6 627,15 km de extensão, o que lhe dá a condição de segundo maior rio do mundo, porém no continente africano ele é o maior. O Nilo é muito importante para os países que são cortados por ele (Uganda, Tanzânia, Ruanda, Quênia, República Democrática do Congo, Burundi, Sudão, Etiópia e Egito). Foi justamente nas margens do rio que nasceu um das mais importantes civilizações: a Egípcia. Para os egípcios, o Nilo é considerado uma “dádiva” de Deus.')

# Loop para exibir cada rio incluido como chave no dicionário
print('\nRios incluidos no do dicionário')
for rio in rios.keys():
    print(rio.title())

# Loop para exibir cada pais incluido como valor no dicionário
print('\nPaises incluidos no do dicionário dos rios')
for pais in set(rios.values()):
    print(pais.title())
