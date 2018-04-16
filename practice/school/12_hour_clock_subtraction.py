"""
Given two positive integers num1 and num2, subtract num2 from num1 on a 12 hour clock rather than a number line.

Input:
First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line containing two integers separated by a space .


Output:
Corresponding to each test case, print the difference in a new line.


Constraints:
1<=T<=100
0<=num1<=1000
0<=num2<=1000

Example:

Input
2
7 5
5 7

Output
2
-2
"""


def clock_subtraction(a, b):
    if a > b:
        return (a - b) % 12
    else:
        return -1 * ((b - a) % 12)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()][0:2]
        print(clock_subtraction(a, b))
