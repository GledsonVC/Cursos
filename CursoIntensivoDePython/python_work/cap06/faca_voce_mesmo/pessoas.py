people = []
pessoa = {
    'first_name': 'gledson',
    'last_name': 'vasconcellos cavalheiro',
    'age': 41,
    'city': 'são paulo',
    }
people.append(pessoa)

pessoa = {
    'first_name': 'ellen',
    'last_name': 'yonobi cavalheiro',
    'age': 6,
    'city': 'são paulo',
    }
people.append(pessoa)

pessoa = {
    'first_name': 'luan',
    'last_name': 'yonobi cavalheiro',
    'age': 6,
    'city': 'são paulo',
}
people.append(pessoa)

# Loop pegando a lista e incluindo nas variaveis
for pessoa in people:
    nome_completo = f"{pessoa['first_name']} {pessoa['last_name']}"
    idade = pessoa['age']
    cidade = pessoa['city']
    # Impriminto na tela
    print(f"\nNome completo: {nome_completo.title()}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade.title()}")
