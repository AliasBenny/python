n=6
for i in range(0,6):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
for i in range(1,n):
    for j in range(0,i):
        print(" ",end='')
    for j in range(2*(n)-1-2*i):
        print('*',end='')
    print()
