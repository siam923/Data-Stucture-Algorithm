## https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    count_dict = {}

    for id in arr:
        if id in count_dict:
            count_dict[id] += 1
        else:
            count_dict[id] = 1
    num = arr[0]
    count = 0
    for key in count_dict:
        if count_dict[key] > count:
            count = count_dict[key]
            num = key 
        elif count_dict[key] == count:
            if num > key:
                num = key 
    return num 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
