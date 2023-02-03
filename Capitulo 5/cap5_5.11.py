numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    if n == 1:
        print(f'{str(n)}st')
    elif n == 2:
        print(f'{str(n)}nd')
    elif n == 3:
        print(f'{str(n)}rd')
    else:
        print(f'{str(n)}th')