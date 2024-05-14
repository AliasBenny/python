import math
n = 25
k = 1
f = 1
i = 0
j = -1
sum = 0
x = int(input('Enter value of x '))
for l in range(25):
    sum = sum + ((-1)*i)*x*f/math.factorial(f)
    if(i%2==0) :
        print('-',x,'^',f,'/',f,'!',end='\t')
    else :
        print('+',x,'^',f,'/',f,'!',end='\t')
    f = f + 2
    i = i + 1
    l = l + 1
print(end='\n')
print(sum)