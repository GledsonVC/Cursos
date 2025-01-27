responses = {}
# Define uma flag para sinalizar que a pesquisa está ativa
polling_active = True
while polling_active:
    # Solicita o nome e a resposta do participante
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Armazena a resposta no dicionario
    responses[name] = response
    # Detecta se mais alguém participará da pesquisa
    repeat = input("Would you like to lt another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# A pesquisa está completa. Mostra os resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} wold like to climb {response.title()}.")
