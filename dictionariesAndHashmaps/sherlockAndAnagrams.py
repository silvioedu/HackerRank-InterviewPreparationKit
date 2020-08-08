#!/bin/python3

import os


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    len_s = len(s)
    substring = []
    res = 0
    for i in range(1, len_s):
        d={}
        for j in range(len_s-i+1):
            substring = ''.join(sorted(s[j:j+i]))
            if substring not in d:
                d[substring] = 1
            else:
                d[substring] += 1

            res += d[substring] - 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
