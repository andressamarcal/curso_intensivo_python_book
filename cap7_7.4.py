message = ''
while message != 'quit':
    message = input("Digite seu ingrediente ou quit: ")

    if message != 'quit':
        print(message+ " foi adicionado a sua pizza")
