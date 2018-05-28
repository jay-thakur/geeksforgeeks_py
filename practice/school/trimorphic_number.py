"""
Given a number N, the task is to check whether the number is Trimorphic number or not. A number is called Trimorphic number if and only if its cube ends in the same digits as the number itself. In other words, number appears at the end of its cube.

Input:
The first line contains an integer T, denoting the number of testcases. T testcases follow. Each testcase contains a single integer N as input.

Output:
Print 1 if the number is trimorphic; else print 0.

Constraints:
1<=T<=100
0<=N<=10000

Example:

Input:
3
1
2
24

Output:
1
0
1

Explanation:
For testcase 3: 24 is N.The cube of 24 is 13824. Since 13824 contains 24, so 24 is a trimorphic number. We print 1.
"""


def trimorphic_number(n):
    cubed = str(n * n * n)
    n_length = len(str(n))
    if n == int(cubed[-1 * n_length:]):
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(trimorphic_number(n))
