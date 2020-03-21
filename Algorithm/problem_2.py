def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    low = 0
    high = len(input_list) - 1

    result = None
    while low <= high:
        mid = (low + high)//2
        if input_list[mid] == number:
            result = mid
        # if sorted low..mid list[low:mid]
        if input_list[low] <= input_list[mid]:
            if number >= input_list[low] and number <= input_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # else search list[mid: high] (sorted)
        elif number >= input_list[mid] and number <= input_list[high]:
            low = mid + 1
        else:
            high = mid - 1
    if result is None:
        return -1
    return result


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
