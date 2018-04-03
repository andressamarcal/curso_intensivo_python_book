users = []

if users: #verifica se a lista esta vazia, se estiver vazia, retorna False e irá parar aqui.
    
    for user in users:
        
        if user == 'admin':
            print('Olá admin, gostaria de ver um relatório de status?')
        
        else:
            print('Olá '+ user + ' obrigado(a) por fazer login novamente.')

else:
    print('Precisamos encontrar alguns usuarios!')