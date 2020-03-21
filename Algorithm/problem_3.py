def get_pivot(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = get_pivot(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)

def quicksort_desc(items):
    sort_all(items, 0, len(items) - 1)
    return items[::-1]

quicksort_desc([4,1,7,23,5])

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    size = len(input_list)
    sorted_desc = quicksort_desc(input_list)

    num1 = 0
    num2 = 0

    for i in range(0, size, 2):
        num1 = num1 * 10 + sorted_desc[i]

    for i in range(1, size, 2):
        num2 = num2 * 10 + sorted_desc[i]

    return num1, num2

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case2)
test_case3 = [[7,3,1,5], [73, 51]]
test_function(test_case3)
