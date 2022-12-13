for row in range(11):
    for col in range(14):
        if (row == 0) and (col in {0, 3, 5, 8, 11, 12}):
            print('*', end='')
        elif (row == 1) and (col in {0, 2, 5, 8, 10}):
            print('*', end='')
        elif (row == 2) and (col in {0, 1, 5, 8, 11}):
            print('*', end='')
        elif (row == 3) and (col in {0, 2, 5, 8, 12}):
            print('*', end='')
        elif (row == 4) and (col in {0, 3, 6, 7, 10, 11}):
            print('*', end='')
        elif (row == 5) and (col in {}):
            print(' ', end='')
        elif (row == 6) and (col in {0, 3, 6, 7, 10}):
            print('*', end='')
        elif (row == 7) and (col in {0, 3, 5, 8, 10}):
            print('*', end='')
        elif (row == 8) and (col in {0, 1, 2, 3, 5, 6, 7, 8, 10}):
            print('*', end='')
        elif (row == 9) and (col in {0, 3, 5, 8, 10}):
            print('*', end='')
        elif (row == 10) and (col in {0, 3, 5, 8, 10, 11, 12, 13}):
            print('*', end='')
        else:
            print(' ', end='')
    print()
