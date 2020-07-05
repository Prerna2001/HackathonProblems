from array import *
def rarray(lst):
    ar1=array('i',[])
    for i in lst:
        ar1.append(i)
    return ar1
lst1 = [int(item) for item in input().split()]
a1=rarray(lst1)
fans = array('i',[])
N=a1[0]
q=a1[1]
lst2 = [int(item) for item in input().split()]
A=rarray(lst2)
for i in range(0,q):
    lst1 = [int(item) for item in input().split()]
    a2=rarray(lst1)

    if(a2[0]==3):
        X=a2[1]
        Y=a2[2]
        A[X-1]=Y


    else:
        L=a2[1]
        R=a2[2]
        if(a2[0]==1):
            s=0
            c=1
            for i in range(L-1,R):
                s=s+(A[i]*c)
                c+=1
                print(s)
            print(s)
            fans.append(s)

        else:
            s=0
            c=1
            for i in range(R-1, L-2, -1):
                s += (A[i]*c)
                c += 1
                print(s)
            print(s)
            fans.append(s)

print(fans)



