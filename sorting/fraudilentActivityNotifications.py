#!/bin/python3

import math
import os
import random
import re
import sys

def get_limit(f,d):
    count = 0
    m1, m2 = (d//2, d//2+1)
    m = []
    for i, j in enumerate(f):
        count += j

        if not m and m1 <= count:
            m.append(i)

        if m2 <= count:
            m.append(i)
            break

    return m[-1]*2 if d % 2 else sum(m)

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    f = [0] * 201
    count = 0

    for i in expenditure[:d]:
        f[i] += 1

    for i, v in enumerate(expenditure[d:]):
        limit = get_limit(f, d)
        if v >= limit:
            count += 1
        f[v] += 1
        f[expenditure[i]] -= 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
