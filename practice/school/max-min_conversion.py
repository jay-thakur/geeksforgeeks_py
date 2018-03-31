"""
Given a no N you can perform an operation in it in which you can change a digit 5 to 6 and vice versa. Now your task is to print the sum of the max no and the min no obtained by performing such operations.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test case follow . Each test case contains a number N.

Output:
For each test case in a new line print the required sum.

Constraints:
1<=T<=100
1<=N<=10000

Example:
Input:
2
35
5
Output:
71
11

Explanation:
For first test case
The max no which can be formed is 36 and the min no which can be formed is 35 itself
sum : 36+35 = 71
For second test case
sum : 5+6 = 11
"""


def conversion(n):
    max = int(n.replace('5', '6'))
    min = int(n.replace('6', '5'))
    return max + min


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(conversion(n))
