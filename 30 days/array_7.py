import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    str1=" "
    x=arr[::-1] #list
    print(' '.join(map(str,x)))