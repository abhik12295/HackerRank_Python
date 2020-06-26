import math
import os
import random
import re
import sys

# Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

if __name__ == '__main__':
    n = int(input())
    counter=0
    max=0
    while n>0:
        if n%2==1:
            counter=counter+1
            if counter>max:
                max=counter
        else:
            counter=0
        n=n//2
    print(max)





   # print(bin(n).replace('0b',''))--- in-built function

#Solution
# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     current_consecutive = 0
#     max_consecutive = 0
#     while n > 0:
#         remainder = n % 2
#         if remainder == 1:
#             current_consecutive += 1
#             if current_consecutive > max_consecutive:
#                 max_consecutive = current_consecutive
#         else:
#             current_consecutive = 0
#         n = n // 2
#     print(max_consecutive)
#
#
