import nome_modulo

nome = 'gledson'
sobrenome = 'vasconcellos cavalheiro'
# Atribuindo a variavel com chamada de modulo nome_modulo usando a 
# funcao nome_funcao 
nome_completo = nome_modulo.nome_funcao(nome, sobrenome)
print(f'Olá, {nome_completo.title()}')
