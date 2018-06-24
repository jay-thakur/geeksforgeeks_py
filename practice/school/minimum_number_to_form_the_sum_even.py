"""
Given an array, write a program to add the minimum number(should be greater than 0) to the array so that the sum of array becomes even

Input:
The first line of input contains an integer T denoting the number of test cases. The first and last line of each test case consists of an integer n. Next line of each test case cinsists of n spaced integers.

Output:
Print the minimum number required to the array so that the sum becomes even .

Constraints:
1<=T<=100
1<=n<=1000
1<=a[i]<=100000

Example:
Input:
2
8
1 2 3 4 5 6 7 8
9
1 2 3 4 5 6 7 8 9

Output:
2
1
"""


def min_no_to_make_sum_even(arr):
    s = sum(arr)
    if s % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(min_no_to_make_sum_even(arr))
