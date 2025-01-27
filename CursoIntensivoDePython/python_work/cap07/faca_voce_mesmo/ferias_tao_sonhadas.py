# Perguntas para usuário responder
pronpt_nome = '\nQual é o seu nome? '
prompt_lugar = '\nSe pudesse visitar qualquer lugar do mundo, para onde iria? '
prompt_pesquisa = '\nDeseja continuar respondendo a pesquisa (sim/ não)? '

# Dicionário que será alimentado
lugares = {}

# enquanto a pesquisa for respondira diferente de 'não' 
# será alimentado o dicionario
while True:
    nome = input(pronpt_nome)
    lugar = input(prompt_lugar)
    lugares [nome] = lugar

    # Condição para o fim do loop
    pesquisa = input(prompt_pesquisa)
    if pesquisa == 'não':
        break

# Exibindo resultados do dicionario alimentado
for nome, lugar in lugares.items():
    print(f'\n{nome.title()}: {lugar.title()}')
