"""
Given an integer array, find sum of elements in it.

Input:

First line contains an integer denoting the test cases 'T'. Every test case contains an integer value depicting size of array 'N' and N integer elements are to be inserted in the next line with spaces between them.

Output:

Print the sum of all elements of the array in separate line.

Constraints:

1 <= T <= 100

1 <= N<= 100

1 <= Arr[i] <= 100

Example:

Input:
2
3
3 2 1
4
1 2 3 4

Output:
6
10

"""


def sum_of_array_elements(arr):
    return sum(arr)


if __name__ == '__main__':
    t = int(input())  # input no of test cases
    for i in range(t):
        size = int(input())  # input size of array
        arr = [int(i) for i in input().split()][0:size]
        # arr = []
        # for j in range(size):
        #     num = int(input())
        #     arr.append(num)

        print(sum_of_array_elements(arr))