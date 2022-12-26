num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end =" ")
        num=num+1
    sum = (num)
    print('The sum of {}'.format(i*j))
    print()