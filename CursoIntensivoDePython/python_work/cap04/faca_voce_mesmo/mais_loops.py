print('\nPrograma-03')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods [:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are:")
for alimento in my_foods:
    print(alimento)
print("\nMy friend's favorite foods are:")
for alimento_amigo in friend_foods:
    print(alimento_amigo)
