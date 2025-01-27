# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Resume o pedido
print(f"You ordered a {pizza['crust']}-crust pizza "
      "whith the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
