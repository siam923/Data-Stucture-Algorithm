## Problem 1: Square Root of an integer
I have used **binary search** algorithm to determine the square root of an integer.

>It takes __O(log(n))__ in the worst case. Since it uses lookup table so space efficiency is constant __O(1)__.

## Problem 2: search in rotated sorted array
Here, I have determine the pivot which divides the array in sorted parts and then used **binary search** algorithm to search the target.

>It runtime complexity is __O(log(n))__ in the worst case. Since it uses lookup table so space efficiency is constant __O(1)__.

## Problem 3: Rearrange Array Elements
The idea here is to sort the array in descending order. I have used **Quick Sort** algorithm to sort the array. Then iterated over the array to find 2 digits.

>It runtime complexity is __O(nlog(n))__. Since it uses lookup table so space efficiency is constant __O(1)__.

## Problem 4: Dutch national flag Problem
Here the input list is divided into 3 parts of 0s, 1s and 2s. Then a while loop is used to sort them by parts.

> Since it uses just a loop so time efficiency is **O(n)** and space efficiency is **O(1)**.

## Problem 5: Autocomplete with Tries
Here Trie data structure is used to look up for suffixes. It is implemented with dictionaries.

> It takes O(n) for finding suffix and space complexity is O(n*m) where n is the number of words and m is the length of the words.

## Problem 6: Max and Min in a Unsorted Array
Here the idea is to iterate of the array and update the minimum and maximum on each iteration.
>Time complexity is **O(n)** and space complexity is O(1)

## Problem 7: HTTPRouter using a Trie
> It takes O(n) for finding the route where n is path length and space complexity is O(n*m) where n is the path length and m is the number of path.
