    #!/bin/python3

import sys

S = input().strip()
print(type(S))


try:
    x = int(S)
    #x=''.join(map(int,S))
    print(type(x))
    print(x)
except:
    print("Bad String")

