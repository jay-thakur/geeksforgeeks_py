"""
Given an array, reverse every sub-array formed by consecutive k elements.

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.The second line of each test case contains N space separated integers denoting array elements.The third line of each test case consists of an integer K.

Output:
Corresponding to each test case, in a new line, print the modified array.

Constraints:

1 ≤ T ≤ 1
"""


def reverse_array_in_groups(size, arr, k):
    rev_arr = []
    for i in range(0, size, k):
        temp = arr[i : i+k]
        rev_arr = rev_arr + temp[::-1]
    return [str(x) for x in rev_arr]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        k = int(input())
        print(' '.join(reverse_array_in_groups(size, arr, k)))
