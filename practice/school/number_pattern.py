"""
For a given number N. Print the pattern in the following form: 1 121 12321 1234321 for N=4.

Input:
First line of input contains the test cases T. Each line of test case contain the value of N for which the pattern is to be displayed.

Output:
For each value of N, print the pattern in a single line.

Constraints:
1<= T <=10
1<= N <= 20

Example:
Input:
2
3
6

Output:
1 121 12321
1 121 12321 1234321 123454321 12345654321
"""


def number_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i-1, 0, -1):
            print(j, end='')
        print(" ", end='')
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        number_pattern(n)