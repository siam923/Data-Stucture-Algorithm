def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number <= 3:
        return 1

    low = 0
    high = number//2

    while low+1<high:
        mid = (low + high)//2
        square = mid*mid
        if square == number:
            return mid
        elif square > number:
            high = mid
        else:
            low = mid

    return low

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
