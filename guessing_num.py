my_guess=5
num=1
while(num<=my_guess):
    user=int(input("enter the number="))
    if(my_guess==user):
        print("sahi guess hai")
        break
    else:
        print("galt guess hai")
    num=num+1