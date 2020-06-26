x=int(input())
for i in range(x):
    nk=input().split(" ",2)
    n=int(nk[0])
    k=int(nk[1])
    newlist = []
    print(k-1 if ((k-1) | k) <= n else k-2)




