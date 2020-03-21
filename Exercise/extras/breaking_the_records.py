## Problem -> https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    max_count = 0
    min_count = 0
    max_score = scores[0]
    min_score = scores[0]

    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_count += 1
            max_score = scores[i]
        elif scores[i] < min_score:
            min_count += 1
            min_score = scores[i]
    return [max_count, min_count]



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
