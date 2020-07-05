print("Number of Try do you want")
n=int(input())

def input_Money():
    print("Enter Your Budget")
    price=int(input())
    return price


def input_sample_price():
    arr={}
    for i in range(1,10):
        print("Enter the ",i, " Elementes")
        sample_price=int(input())
        arr[sample_price]=i
    return arr

for i in range(0,n):
    price=input_Money()
    arr=input_sample_price()
    c=min(arr)
    if c!=1:
        amount=price%c
    else:
        amount=price
    sample_output=0
    for i in range(0,amount):
        sample_output=(sample_output*10)+arr[c]
    if(sample_output!=0):
        print(sample_output)
    else:
        print(-1)