a=input("day=")
b=input("name")
d=input("name")
e=input("name")
c=int(input(("vote to ",b)))
f=int(input(("vote to ",d)))
g=int(input(("vote to ",e)))
if a=="monday":
    print("disco will relect")
    if (c>f and c>g):
        print(b,"wiil to disco")
    elif(f>c and f>g ):
        print(d,"will be dicso")
    elif(g>c and g>f):
        print(e,"wiil be disco")
if a=="tuesday":
    print("t&p will election")
    if(c>f and c>g):
        print(b,"will be T&P")
    elif(f>c and f>g):
        print(d,"will be T&p")
    elif (g>c and g>f):
        print(e,"will be T&p")
if a=="wednesday":
    print("food coordinator will be election")
    if(c>f and c>g):
        print(b, "will be f&c")
    elif(f>c and f>g):
        print(d,"will be f&c")
    elif(g>c and g>f):
        print(e,"will be f&c")
else:
    print("party karenge sb")
