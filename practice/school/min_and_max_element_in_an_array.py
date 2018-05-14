"""
Given an array of integers.Your task is to find the minimum and maximum element in the array.
Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains an integer n denoting the size of the array. The following line contains 'n' integers forming the array.

Output:
Print the minimum and maximum element of the array.

Constraints:
1<=T<=100
1<=n<=1000
1<=a[i]<=10^12

Example:
Input:
2
6
3 2 1 56 10000 167
5
1 345 234 21 56789
Output:
1 100000
1 56789
"""


def min_and_max_element(arr, size):
    arr.sort()
    print(arr[0], end=' ')
    print(arr[size - 1])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        min_and_max_element(arr, size)
