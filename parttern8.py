deer=8
for i in range(5):
    count = 0
    for k in range(deer):
        print(end = " ")
    deer = deer - 2
    for j in range(i+1):
        count = count+1
    num = count
    for j in range(i+1):
        print(num,end = " ")
        num = num-1
    print()