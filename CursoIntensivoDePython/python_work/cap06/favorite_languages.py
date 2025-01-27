print('\nPrograma-01')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print('\nPrograma-02')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah´s favorite language is {language}.")

print('\nPrograma-03')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}´s favorite language is {language.title()}.")

print('\nPrograma-04')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

print('\nPrograma-05')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in favorite_languages:
    print(name.title())

print('\nPrograma-06')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print('\nPrograma-07')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print('\nPrograma-08')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print('\nPrograma-09')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print('\nPrograma-10')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print('\nPrograma-11')
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}´s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
# Proposta feita por conta verificando se contem mais de uma linguagem
# cada pessoa que respondeu
print('\nPrograma-11-1')
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}´s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        language  = languages[0]
        print(f"\n{name.title()}´s favorite languages is:")
        print(f"\t{language.title()}")
