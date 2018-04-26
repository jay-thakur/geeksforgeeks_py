"""
Given an array, find the largest element in it.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n , the no of elements in the array. Then next line contains n integers of the array.

Output:
Print the maximum element in the array.

Constraints:
1<=T<=100
1<=n<=100
1<=a[i]<=1000

Example:
Input:
2
5
10 324 45 90 9808
7
1 2 0 3 2 4 5

Output :
9808
5
"""


def largest_element(arr):
    return max(arr)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(largest_element(arr))
