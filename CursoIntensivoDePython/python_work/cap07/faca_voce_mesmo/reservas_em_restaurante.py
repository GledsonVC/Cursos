mesa = input('Quantos lugares em uma mesa você precisa? ')
mesa = int(mesa)
if mesa > 8:
    print('É necessário aguardar por uma mesa.')
else:
    print('A mesa já está disponível.')
