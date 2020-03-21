#!/bin/python3

import os


# https://www.hackerrank.com/challenges/drawing-book/problem?h_r=next-challenge&h_v=zen
# Complete the pageCount function below.
#
def pageCount(n, p):
    flips_f = p // 2
    flips_b = (n//2-p//2)
    return min(flips_f, flips_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
