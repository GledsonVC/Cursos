paises = ['canada', 'estados unidos', 'australia', 'egito']
print(f'Inicio do programa, lista paises\n\t{paises}')

#função sortede para mostrar em ordem alfabetica e não alterar a lista
print('\nfunção sorted(paises)')
print(sorted(paises))

#função sortede para mostrar em ordem alfabetica inversa e não alterar a lista
print('\nfunção sorted(paises, reverse=True)')
print(sorted(paises, reverse=True))

#função len para contar a quantidade de paises na lista
print('\nfunção len(paises)')
print(len(paises))

print(f'\nFim do programa, estou mostrando que as funções não alteraram a lista\n\t{paises}')
