#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    qtd = 0
    aux = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != aux[i]:
            j = arr.index(aux[i])
            #print("swap ({},{})".format(i, j))
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            qtd += 1
    return qtd


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)