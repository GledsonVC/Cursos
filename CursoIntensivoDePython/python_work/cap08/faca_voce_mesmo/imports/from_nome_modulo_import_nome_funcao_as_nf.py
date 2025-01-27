from nome_modulo import nome_funcao as nf

nome = 'gledson'
sobrenome = 'vasconcellos cavalheiro'
# Atribuindo a variavel nome_completo com chamada de função importada e renomeada 
# nf de nome_funcao do modulo nome_modulo
nome_completo = nf(nome, sobrenome)
print(f'Olá, {nome_completo.title()}')
