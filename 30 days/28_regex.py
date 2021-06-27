#!/bin/python3

import re
if __name__ == '__main__':
    N = int(input())
    lst=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        match=re.search('@gmail\.com$',emailID)

        if match:
            lst.append(firstName)
    y=sorted(lst)
    print('\n'.join(y))
    
#witohout using regex
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    lst = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if '@gmail.com' in emailID:
            lst.append(firstName)
    y = sorted(lst)
    print('\n'.join(y))
        



