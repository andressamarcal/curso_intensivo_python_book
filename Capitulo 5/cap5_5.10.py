current_users = ['admin','maria','joao','ana','pedro']

new_users = ['joao','PEDRO','lucas','Ana','marina']

#verifica se ja existe os novos nomes de usuarios na listagem anterior, verificando todas as formas de escrita
for user in new_users:
    
    if user in current_users or user.lower() in current_users or user.lower() in current_users or user.title() in current_users:
        print(f'{user} usuario existente, forneça um novo nome de usuario')

    else:
        print(f"Olá {user} ,seu nome esta diponivel para uso.")