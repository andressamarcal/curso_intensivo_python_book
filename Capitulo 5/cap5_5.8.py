users = ['admin','ana','joao','maria','pedro']

for user in users:
    if user == 'admin':
        print('Olá admin, gostaria de ver um relatório de status?')
    else:
        print('Olá '+ user + ' obrigado(a) por fazer login novamente.')
