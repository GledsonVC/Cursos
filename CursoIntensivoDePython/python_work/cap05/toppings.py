print("\nPrograma-01")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("\nPrograma-02")
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("\nPrograma-03")
# Livro mostra condição incorreta do if-elif
requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("\nPrograma-04")
requested_toppings = ['mushrooms','green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

print("\nPrograma-05")
requested_toppings = ['mushrooms','green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

print("\nPrograma-06")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")          
else:
   print("Are you sure you want a plain pizza?")

print("\nPrograma-07")
avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don´t have {requested_topping}.")
print("\nFinished making your pizza!")
