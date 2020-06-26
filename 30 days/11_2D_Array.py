#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []


    def find_sum(arr, i, j):
        sum = 0
        sum += arr[i][j]
        sum += arr[i][j + 1]
        sum += arr[i][j + 2]
        sum += arr[i + 1][j + 1]
        sum += arr[i + 2][j]
        sum += arr[i + 2][j + 1]
        sum += arr[i + 2][j + 2]
        return sum


    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # result=[]
    maxx = -63
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            summ = find_sum(arr, i, j)
            # result.append(summ)
            if summ > maxx:
                maxx = summ
    print(maxx)
    #print(max(result))