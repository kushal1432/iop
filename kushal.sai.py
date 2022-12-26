for row in range (5):
    for col in range (33):
        if (row == 0) and (col in {0,3,6,9,13,14,17,20,24,25,29}):
            print('+', end = '')
        elif(row == 1) and (col in {0,2,6,9,12,17,20,23,26,29}):
            print('+', end = '')
        elif(row == 2) and (col in {0,1,6,9,13,17,18,19,20,23,24,25,26,29}):
            print('+', end = '')
        elif(row == 3) and (col in {0,2,6,9,14,17,20,23,26,29}):
            print('+', end = '')
        elif(row == 4) and (col in {0,3,7,8,12,13,17,20,23,26,29,30,31,32}):
            print('+', end = '')
        else:
            print(' ', end = '')
    print()