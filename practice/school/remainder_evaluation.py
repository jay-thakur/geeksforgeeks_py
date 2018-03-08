"""
Given two positive integers num1 and num2, the task is to find the remainder when num1 is divided by num2.

Input:

First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line containing two positive integers seperated by a space .

Output:

Corresponding to each test case, print the remainder in a new line.

Constraints:
1<=T<=100
0<=num1<=50
1<=num2<=50

Example:
Input:
1
5 3
Output:
2
"""


def remainder_eval(a, b):
    return a % b


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(remainder_eval(a, b))