for row in range (12):
    for col in range(10):
        if (row == 0) and (col in {0,2,3,5,6,7,8}):
            print('$', end = '')
        elif(row == 1) and (col in {0,1,3,5,6}):
            print('$', end = '')
        elif(row == 2) and (col in {0,3,5,6,7,8}):
            print('$', end = '')
        elif(row == 3) and (col in {0,1,3,5,8}):
            print('$', end = '')
        elif(row == 4) and (col in {0,2,3,4,5,6,7,8}):
            print('$', end = '')
        elif(row == 5) and (col in {}):
            print('*', end = '')
        elif(row == 6) and (col in {0,2,3,4,5,6}):
            print('@', end = '')
        elif(row == 7) and (col in {0,2,3,5,6}):
            print('@', end = '')
        elif(row == 8) and (col in {0,1,2,3,4,5,6,}):
            print('@', end = '')
        elif(row == 9) and (col in {0,2,3,5,6}):
            print('@', end = '')
        elif(row == 10) and (col in {0,2,3,5,6,7,8}):
            print('@', end = '')
        else:
            print(' ', end = '')
    print()
