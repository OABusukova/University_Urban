for elem in range(3, 21):
    password = ''
    for x in range(1, elem):
        for y in range(x+1, elem):
            if elem % (x + y) == 0:
                password += f'{x} + {y}'
    print(elem, '-', password)
