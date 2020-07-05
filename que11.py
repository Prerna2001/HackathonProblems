from array import *
def rarray(lst):
    ar1=array('i',[])
    for i in range(0,9):
        x=lst[i]
        ar1.append(x)
    return ar1
a=int (input())
ar=array('i' ,[])
far=array('i',[])

for i in range (0,a):
    v=""
    N = int(input())
    lst1 = [int(item) for item in input( ).split()]
    arr=rarray(lst1)
    c=N
    min=N
    while(c!=0):

        loc=0
        for k in range (0,9):
            if arr[k]<min:
                min=arr[k]
                loc=k
            if arr[k]==min:
                min=arr[k]
                loc=k
        c=c-min
        v=v+str(loc+1)
    if(v==""):
        far.append("-1")
    else:
        far.append(int(v))
print(far)







