#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    return min(abs(x-y) for x, y in zip(arr, arr[1:]))
    #r = []
    #for x,y in zip(arr, arr[1:]):
    #    r.append(abs(x-y))
    #return min(r)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
