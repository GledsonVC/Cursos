import nome_modulo as nm

nome = 'gledson'
sobrenome = 'vasconcellos cavalheiro'
# Atribuindo a variavel com chamada de modulo renomeado para 
# nm de nome_modulo usando a funcao nome_funcao 
nome_completo = nm.nome_funcao(nome, sobrenome)
print(f'Olá, {nome_completo.title()}')
