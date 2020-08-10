#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    dict_sentences = {'swaps': 'Array is sorted in {} swaps.',
                      'first': 'First Element: {}',
                      'last': 'Last Element: {}'}

    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    print(dict_sentences['swaps'].format(swaps))
    print(dict_sentences['first'].format(a[0]))
    print(dict_sentences['last'].format(a[len(a)-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
