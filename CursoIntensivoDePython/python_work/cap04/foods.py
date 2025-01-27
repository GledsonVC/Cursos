print('\nPrograma-01')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\nPrograma-02')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\nPrograma-03')
my_foods = ['pizza', 'falafel', 'carrot cake']
# Isso não funciona:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
