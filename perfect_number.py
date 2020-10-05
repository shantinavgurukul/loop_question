num=int(input("enter the no:-"))
i=1
sum=0
while(i<=num):
    if (num%i==0):
        sum=sum+i
    i=i+1
if(num==sum/2):
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")