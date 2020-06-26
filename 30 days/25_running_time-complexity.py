# x=int(input())
# for i in range(x):
#     z=int(input())
#     if z>1:
#         for j in range(2,z):
#             if(z%j)==0:
#                 print("Not prime")
#                 break
#         else:
#             print("Prime number")
#             break
#     else:
#         print("Not prime")
import math

x=int(input())
for i in range(x):
    z=int(input())
    if z<2:
        print("Not prime")
    elif z>1:
        for j in range(2,int(z**0.5)+1):  #No need to check the repeated factors again
            if z%j==0:
                print("Not prime")
                break
        else:
            print("Prime")