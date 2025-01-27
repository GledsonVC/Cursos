print('\nPrograma-01')
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

print('\nPrograma-02')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")


print('\nPrograma-03')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

print('\nPrograma-04')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
