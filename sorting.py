
a = input("Enter a string: ")

words = a.split()

asort = sorted(words)
print("Words in sorted order:")
for word in asort:
    print(word)
