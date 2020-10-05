minimum = int(input("Enter a Number: " ))
while(True):
    A = int(input("Enter a Number (Use -1 to Stop): " ))
    if(A == 31):
        break
    if minimum > A:
        minimum = A
print(minimum)
