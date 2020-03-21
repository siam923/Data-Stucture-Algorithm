def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_ = ints[0]
    max_ = ints[0]

    for num in ints:
        if num < min_:
            min_ = num
        if num > max_:
            max_ = num
    return (min_, max_)

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l2 = [i for i in range(5, 15)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((5, 14) == get_min_max(l2)) else "Fail")

l3 = [i for i in range(0, 1)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 0) == get_min_max(l3)) else "Fail")
