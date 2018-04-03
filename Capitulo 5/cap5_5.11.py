numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    if n == 1:
        print(str(n) +'st')
    elif n == 2:
        print(str(n) +'nd')
    elif n == 3:
        print(str(n) + 'rd')
    else:
        print(str(n) + 'th')