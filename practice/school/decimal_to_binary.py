"""
Given a decimal number. Write a program to convert it into equivalent binary number.

Input:
First line of input contains a single integer T which denotes the number of test cases. First line of each test case contains a single integer N which represents a decimal value.

Output:
For each test case, print the binary equivalent of the given decimal value N.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
3
7
10
33
Output:
111
1010
100001
"""


def decimal_to_binary(n):
    return format(n, "b")


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(decimal_to_binary(n))
