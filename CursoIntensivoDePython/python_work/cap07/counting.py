print('\nPrograma-01')
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print('\nPrograma-02')
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)


print('\nPrograma-03')
x = 1
while x <= 5:
    print(x)
    x += 1

# problema nesse programa com loop infinito 
# colocado um break para finalizar
print('\nPrograma-03')
x = 1
while x <= 5:
    print(x)
    # incluido o break
    break
