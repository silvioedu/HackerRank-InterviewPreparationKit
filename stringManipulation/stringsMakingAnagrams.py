#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    c_a = Counter(a)
    c_b = Counter(b)
    c_a.subtract(c_b)
    return sum(abs(i) for i in c_a.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
