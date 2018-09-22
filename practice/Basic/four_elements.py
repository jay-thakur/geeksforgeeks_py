"""
Given an array of integers, find a combination of four elements in the array whose sum is equal to a given value X.

Input:
First line consists of T test cases. First line of every test case consists of an integer N, denoting the number of elements in an array. Second line consists of N spaced array elements. Third line of every test case X.

Output:
Single line output, print 1 if combination is found else 0.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
1
6
1 5 1 0 6 0
7
Output:
1
"""


from itertools import combinations


def four_elements(arr, x):
    for ele in combinations(arr, 4):
        if sum(ele) == x:
            return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        x = int(input())
        print(four_elements(arr, x))
