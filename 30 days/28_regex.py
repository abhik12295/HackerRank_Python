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
    print('\n'.join(lst))
    # y = sorted(lst)
    # print(*y, sep='\n')



