#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    count = len(s)
    for i, c in enumerate(s):
        dif_char_idx = None

        for j in range(i+1, n):
            if c == s[j]:
                if dif_char_idx is None:
                    count += 1
                elif j - dif_char_idx == dif_char_idx - i:
                    count += 1
                    break
            else:
                if dif_char_idx is None:
                    dif_char_idx = j
                else:
                    break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
