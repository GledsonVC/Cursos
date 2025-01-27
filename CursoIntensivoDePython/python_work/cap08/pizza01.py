print(80 * '-')
print('\nPrograma-01')
def make_pizza(*toppings):
    """Exibe a lista de ingredientes solicitados"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print(80 * '-')

print('\nPrograma-02')
def make_pizza(*toppings):
    """Sintetiza a pizza que estamos prestes a fazer"""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print(80 * '-')


print('\nPrograma-03')
def make_pizza(size, *toppings):
    """Sintetiza a pizza que estamos prestes a fazer"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print(80 * '-')
