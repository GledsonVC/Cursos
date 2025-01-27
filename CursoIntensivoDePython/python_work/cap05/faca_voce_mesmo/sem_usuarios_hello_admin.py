# usuarios = ['gledson', 'ellen', 'admin', 'gisele', 'luan']
usuarios = []
if not usuarios:
    print('É necessário encontrar alguns usuários!')
else:
    for usuario in usuarios:
        if usuario == 'admin':
            print('Olá administrador, gostaria de ver um relatório de status?')
        else:
            print(f'Olá, {usuario.title()}, obrigado por fazer login novamente.')
