print(80 * '-')
print('\nPrograma-01')
def greet_user():
    """Exibe um simples cumprimento"""
    print("Hello!")
greet_user()
print(80 * '-')

print('\nPrograma-02')
def greet_user(username):
    """Exibe um simples cumprimento"""
    print(f"Hello, {username.title()}!")
greet_user('jesse')
print(80 * '-')

print('\nPrograma-03')
def greet_users(names):
    """Exibe um simples hello para cada usuário na lista"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print(80 * '-')
