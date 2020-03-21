#!/bin/python3

## https://www.hackerrank.com/challenges/sock-merchant/problem

import os
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c = Counter(ar)
    num_pairs = 0

    for color in set(ar):
        num_pairs += c[color] // 2

    return num_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
