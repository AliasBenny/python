n=5
for i in range(n):
    for j in range(1,i+1):
        print(j,end='')
    for j in range(2*(n-i-1)):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    
    print()