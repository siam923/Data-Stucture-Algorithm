# Description:
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=next-challenge&h_v=zen

def divisibleSumPairs(n, k, ar):
    """
    n -> lenght of array
    k -> number to check divisibity 
    ar -> array 
    output -> number of pairs (i,j) where i<j and (ar[i]+ar[j]) % k ==0
    """
    sum_ = 0
    count = 0
    for i in range(n-1):
        for j in range(i, n-1):
            sum_ = ar[i] + ar[j+1]
            if sum_ % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
