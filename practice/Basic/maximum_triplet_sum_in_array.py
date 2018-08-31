"""
Given an array, the task is to find maximum triplet sum in the array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the maximum triplet sum in new line.

Constraints:
1<=T<=100
3<=N<=106
-105<=A[i]<=105

Example:
Input:
2
6
1 0 8 6 4 2
7
1 2 3 0 -1 8 10
Output:
18
21
"""


def maximum_triplet_sum_in_array(arr, size):
    arr = sorted(arr)
    return sum(arr[size - 3:size])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(maximum_triplet_sum_in_array(arr, size))
