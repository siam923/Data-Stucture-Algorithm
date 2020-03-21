#!/bin/python3

def calculate_distance(arr):
    i = 0
    sum_dist = 0
    while i<len(arr)-1:
        sum_dist += arr[i+1] - arr[i]
        i += 1
    return sum_dist


# Main
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        text = f.read()

file_input = text.split('\n')
num_case = int(file_input[0].strip())

file = open('output.txt', 'w')

for line in file_input[1:]:
    arr = list(map(int, line.rstrip().split()))
    result = calculate_distance(arr[1:])
    file.write(str(result)+"\n")

file.close()
