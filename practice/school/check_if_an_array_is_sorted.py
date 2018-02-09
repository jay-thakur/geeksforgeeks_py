"""
Given an array, write a program that prints 1 if array is sorted in non-decreasing order, else prints 0.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input C[i].

Output:

Print 1 if array is sorted, else print 0.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ C[i] ≤ 1200

Example:

Input
2
5
10 20 30 40 50
6
90 80 100 70 40 30

Output
1
0
"""


def is_sorted(size, arr):
    for i in range(1, size):
        if arr[i-1] > arr[i]:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        result = is_sorted(size, arr)
        if result:
            print("1")
        else:
            print("0")