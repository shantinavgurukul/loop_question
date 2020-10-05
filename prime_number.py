a=2
while(a<=100):
    b=2
    while(b<a):
        if(a%b==0):
            print(a,"not prime no")
            break
        b=b+1
    else:
        print(a,"prime no") 
    a=a+1


# num=1
# while(num<=100):
#     count=0
#     i=2
#     while(i<=num/2):
#         if(num%i==0):
#             print(num,"its not prime")
#             count=count+1
#             break
#         i=i+1
#     if(count==0 and num!=1):
#         print(num,"its  prime")
#     num=num+1