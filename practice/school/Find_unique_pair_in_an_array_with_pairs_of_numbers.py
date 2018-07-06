"""
Given an array where every element appears twice except a pair (two elements). Find the elements of this unique pair.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, in new line print the unique pair in increasing order.

Constraints:
1<=T<=100
1<=N<=103
1<=A[i]<=103

Example:
Input:
2
6
2 2 5 5 6 7
4
1 3 4 1

Output:
6 7
3 4
"""


def find_unique_pairs(arr):
    unique_pairs = []
    for i in sorted(arr):
        if arr.count(i) == 1:
            unique_pairs.append(i)
    return unique_pairs


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*find_unique_pairs(arr))
