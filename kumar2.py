for row in range (11):
    for col in range (28):
        if (row == 0) and (col in {0,3,5,8,11,12,14,17,20,21,24}):
            print('+', end = '')
        elif(row == 1) and (col in {0,2,5,8,10,14,17,19,22,24}):
            print('+', end = '')
        elif(row == 2) and (col in {0,1,5,8,11,14,15,16,17,19,20,21,22,24}):
            print('+', end = '')
        elif(row == 3) and (col in {0,2,5,8,12,14,17,19,22,24}):
            print('+', end = '')
        elif(row == 4) and (col in {0,3,6,7,10,11,14,17,19,22,24,25,26,27}):
            print('+', end = '')
        else:
            print(' ', end = '')
    print()