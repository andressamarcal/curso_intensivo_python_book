if users := []:
    for user in users:
        
        if user == 'admin':
            print('Olá admin, gostaria de ver um relatório de status?')

        else:
            print(f'Olá {user} obrigado(a) por fazer login novamente.')

else:
    print('Precisamos encontrar alguns usuarios!')