def ismagic(x):
    sum= lambda x : 0 if x ==0 else x % 10 + sum(x // 10)
    n=sum(x)%2
    f= lambda n : 0 if n!= 0 else  1

    return f(n)

n=int(input("Enter a number"))
if(n<=0):
    print("Invaid Input")
else:
   r = ismagic(n)
   if r == 0:
       print(str(n) +" is not a magic number")
   else:
       print(str(n) +" is a magic number")
