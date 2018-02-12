"""
Given a binary array, sort it in non-decreasing order

Input: First line contains an integer denoting the test cases 'T'.  Every test case contains two lines, first line is size and second line is space separated elements of array

Output:  Space separated elements of sorted arrays.  There should be a new line between output of every test case.


Constraints:
1 <= Size of Array <= 1000
10 <= Number of test cases <= 100

Example:

Input:
2
5
1 0 1 1 0
10
1 0 1 1 1 1 1 0 0 0

Output:
0 0 1 1 1
0 0 0 0 1 1 1 1 1 1
"""


def binary_array_sorting(arr):
    arr.sort()
    print(*arr, sep=' ')


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        binary_array_sorting(arr)