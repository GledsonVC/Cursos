current_users = ['gledson', 'ellen', 'admin', 'gisele', 'luan']
new_users = ['clovis', 'zoraide', 'ADMIN', 'maria', 'Gledson']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Você precisa inserir outro nome de \nusuário '
              f'{new_user.title()} já foi utilizado na lista\n')
    else:
        print(f'{new_user.title()} pode ser utilizádo como nome de usuário\n')
