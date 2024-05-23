import array

a = array.array('i', [1, 3, 2])
print(a)
large=a[0]
for i in range(1,len(a)):
    if a[i]>large:
     large=a[i]
print("large ",a[i])