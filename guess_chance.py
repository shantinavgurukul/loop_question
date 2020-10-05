guess_num=5
chance=10
i=1
while(i<=chance):
    num=int(input("enter the number="))
    if(guess_num>num):
        var=num-guess_num
        var=var*(-1)
        chance=chance-var
    elif(guess_num==num):
        print("you are winer")
    else:
        var=num-guess_num
        chance=chance-var

else:
    print("you are looser")