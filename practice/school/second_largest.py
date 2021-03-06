"""
Given an array, return second  largest element from an array.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input C[i].

Output:

Print the second largest element.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 500
1 ≤ C[i] ≤ 1200

Example:

Input
2
5
89 24 75 11 23
6
56 42 21 23 65 20

Output
75
56
"""


def second_largest(size, arr):
    arr.sort()
    return arr[size - 2]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(second_largest(size, arr))