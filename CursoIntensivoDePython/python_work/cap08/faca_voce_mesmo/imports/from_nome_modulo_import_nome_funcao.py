from nome_modulo import nome_funcao

nome = 'gledson'
sobrenome = 'vasconcellos cavalheiro'
# Atribuindo a variavel nome_completo com chamada de função importada nome_funcao 
# do modulo nome_modulo
nome_completo = nome_funcao(nome, sobrenome)
print(f'Olá, {nome_completo.title()}')
