for row in range (10):
    for col in range(4):
        if(row+col==3)or(row-col==3)or(row+col==9): 
         print('*',end=" ")
    print()
