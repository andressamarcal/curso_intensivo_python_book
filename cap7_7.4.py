message = ''
while message != 'quit':
    message = input("Digite seu ingrediente ou quit: ")

    if message != 'quit':
        print(f"{message} foi adicionado a sua pizza")
