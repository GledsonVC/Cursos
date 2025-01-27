from nome_modulo import *

nome = 'gledson'
sobrenome = 'vasconcellos cavalheiro'
# Atribuindo a variavel com chamada de função nome_funcao de todo 
# módulo nome_modulo importado com o *  
nome_completo = nome_funcao(nome, sobrenome)
print(f'Olá, {nome_completo.title()}')
