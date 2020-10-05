num=2
number=int(input("enter the no.="))
while(number>num):
    if(number%num==0):
        print("not prime")
        break
    num=num+1
else:
    print("prime")
