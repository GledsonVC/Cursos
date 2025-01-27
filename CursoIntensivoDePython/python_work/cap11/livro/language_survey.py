from survey import AnonymousSurvey


# Define uma pergunta e faz uma pesquisa
question = "What language dit you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena respostas à pergunta
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Mostra os resultados da pesquisa
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
