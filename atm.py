print("welcome to SBI Bank")
laugange=input("enter the langauge=")
if laugange=="english":
    print("this is  your select language")
pin=int (input("enter the pin no.="))
if(pin>1000 and pin<9999):
    print("next")
    ac=input("type of account=")
    amt=int(input("withdrawal amount="))
    if(amt>0):
        print("collect cash")
        print("your transaction successful")
    else:
        print("cancel")
else:
    print("invalid pin no.")