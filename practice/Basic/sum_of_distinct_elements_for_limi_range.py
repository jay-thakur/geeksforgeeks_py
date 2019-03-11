"""
Given an array of n elements such that every element of array is an integer in the range 1 to n, find the sum of all the distinct elements of the array.

Input:
First line consists of T test cases. First line of every test case consists of N. Second line of every test case consists of elements of Array.

Output:
Single line output, print the sum of distinct element of array.

Constraints:
1<=T<=200
1<=N<=10^4

Example:
Input:
2
5
1 2 3 3 4
5
1 1 1 2 2

Output:
10
3
"""


def sum_of_distinct_elements(arr):
    arr = set(arr)
    return sum(list(arr))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(sum_of_distinct_elements(arr))
