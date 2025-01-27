print('\nPrograma 01')
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Mesmo programa não colocando a variável temporária
print('\nPrograma 02')
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
