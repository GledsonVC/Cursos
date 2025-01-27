from pathlib import Path


def procura_palavra_no_livro(arquivo):
    """Função que irá procurar em um arquivo e retorna quantas vezes foi uti
    lisada a palavra descrita no arquivo"""
    caminho = Path(__file__).parent / arquivo
    try:
        conteudo = caminho.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'\nArquivo não encontrado. "{caminho}"\n')
    else:
        # Contando o conteudo transformando tudo em minusculo a quantidade de 
        # palavras escolhida
        palavra = input('\nQual palavra deseja contar no livro: ')
        quantidade_palavras = conteudo.lower().count(palavra)
        print(
            f'A palavra "{palavra}", foram descritas no livro alice\n' + 
            f'{quantidade_palavras} vezes.'
            )


# Instrução do programa
mensagem = '\nEscreve uma palavra e irei contar as quantidades de vezes que foi'
mensagem += ' utilizada no livro Alice.'
print(mensagem)

arquivo = 'alice.txt'
procura_palavra_no_livro(arquivo)
