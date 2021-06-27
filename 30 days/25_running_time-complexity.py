x=int(input())
for i in range(x):
    num=int(input())
    if num<2:
        print("Not prime")
    elif num>1:
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                print("Not prime")
                break
        else:
            print("Prime")
