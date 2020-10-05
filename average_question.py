i=1
total_weight=0
average_weight=0
while(i<=3):
    num=int(input("enter the number="))
    total_weight=total_weight+num
    i=i+1
    print(total_weight)
    average_weight=total_weight/11
print(average_weight)
if(average_weight%5==0):
    print("5 se divisible hai")
else:
    print("5 se divisible nahi hai")