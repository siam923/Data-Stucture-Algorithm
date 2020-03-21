"""
Problem Description:
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

The first line contains two space-separated integers, n and m, the number of elements in array n and the number of elements in array m.
Second line resembles n and third line resembles m.

Sample Input:
2 3
2 4
16 32 96

Sample Output

3
"""

# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def common_factors(brr):
    min_no = min(brr)
    facts = []

    for num in range(1, min_no+1):
        flag = True
        for i in brr:
            if i%num != 0:
                flag = False
        if flag:
            facts.append(num)
    return facts

def is_factor(num1, num2):
    return num2 % num1 == 0

def getTotalX(arr, brr):
    cf = common_factors(brr)
    count = 0
    for num2 in cf:
        flag = True
        for num1 in arr:
            if not is_factor(num1, num2):
                flag = False
        if flag:
            count += 1
    return count



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    #fptr.write(str(total) + '\n')

    #fptr.close()
    print(total)
