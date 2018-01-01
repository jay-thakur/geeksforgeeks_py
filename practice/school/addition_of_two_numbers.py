"""
Given two numbers a and b, return their sum.

Input:

The first line of the input contains T denoting the total number of testcases. Each testcase contains two space separated positive integers denoting the value of a and b.

Output:

Output the sum of a and b.

Constraints:

1<=T<=100
1<=a,b<=1000

Example:


Input:
1
2 3

Output:
5

"""


def addition_of_two_numbers(a, b):
    return a + b


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()][0:2]
        print(addition_of_two_numbers(a, b))