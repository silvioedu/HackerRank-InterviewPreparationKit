#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    d = {'y': 'YES', 'n': 'NO'}
    a = Counter(s)
    b = Counter(a.values())

    if len(b) == 1:
        return d['y']
    elif len(b) == 2:
        maxV = max(b.values())
        k1, k2 = b.keys()
        if maxV == len(a) - 1:
            if abs(k1 - k2) == 1:
                return d['y']
            elif min(k1, k2) == 1:
                if b[1] == 1:
                    return d['y']
    return d['n']


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
