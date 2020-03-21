## Run Time analysis of task0:

Task0 is pretty straight forward. It is Big `O(1)`. The runtime of the code does not depend on the size of the input. It is just two print statement. So we can conclude task0 has constant runtime.

## Run Time analysis of task1:
Task1 has a for loop which runs as many times the size of the record list. For each iteration in the loop we again have to check if the item in the list. Each checking takes linear time. Therefore, we can say it has quadratic runtime i.e Big `O(n^2)`.

## Run Time analysis of task2:
In Task2 we loop over all the items in the calls record and for each record we check if the caller and the callee `in` the call_time dictionary and do some assignments. The `in` operator for dictionary in average case has `O(1)` and in worst case has runtime `O(n)`


After the loop we call the max function which runs in linear time. So, our runtime in worst case is like `[n*(n+n) + n]` which can be expressed with `Amortized Worst case O(n^2)`.

## Run Time analysis of task3:
In task 3 there is 2 parts. Each of the part uses a for loop. The number of time the loops will run depends on the size of the input list. The runtime for the 2 loops is like `[n+n]`.

The python default `sort()` function has `O(nlogn)` runtime.
So we can approximate `[n+n+nlogn]` --> `Big O(nlogn)` time.

## Run Time analysis of task3:
Here we have to iterate over the texts and calls list. Then for the sort function our overall runtime is like (n+n+nlogn).
So the runtime of the code is `Big O(nlogn)`.
