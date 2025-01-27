import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """Uma pesquisa que estará disponível para todas as funções de teste"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """Testa se uma única resposta está devidamente armazenada"""
    # question = "What language did you first learn to speak?"
    # language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses(language_survey):
    """Testa se três respostas individuais estão devidamente armazenadas"""
    # question = "What language did you first learn to speak?"
    # language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses

