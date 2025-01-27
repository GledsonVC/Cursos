import camiseta as c
from camisetas_grandes import make_shirt as ms
from livro_favorito import *

print('-' * 80)
print('\nEstilizando programa-01')
# Chamar função com argumentos posicionais
c.make_shirt('pequeno', 'Sou programador PYTHON')

# Chamar função com com argumentos nomeados
c.make_shirt(mensagem='Garoto de programa', tamanho='grande')
print('-' * 80)


print('\nEstilizando programa-02')
# Chamar camiseta grande com mensagem padrão
ms()

# Chamar camiseta media com mensagem padrão
ms('media')

# Chamar função com com argumentos nomeados
ms(tamanho='pequena', mensagem='Python é fácil de aprender.')
print('-' * 80)

print('\nEstilizando programa-03')
favorite_book('curso intensivo de python')
print('-' * 80)
