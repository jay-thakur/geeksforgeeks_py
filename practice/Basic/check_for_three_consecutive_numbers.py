"""
Given an integer n, the task is to find whether n can be written as sum of three consecutive integer.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

Output:
For each testcase, if it is possible to write as a sum of three consecutive integers  then print three consecutive integer, else print “-1”.
Constraints:

1<=T<=100

1<=N<=10000
Example:

Input:
2
6
7

Output:
1 2 3
-1

Explanation:
Testcase 1: N = 6 can be written as 1+2+3.

Testcase 2: N = 7 can be written as a sum of three consecutives.
"""


def check_for_three_consecutive_numbers(n):
    if n % 3 != 0:
        print(-1)
    else:
        x = int(n / 3)
        print(x - 1, x, x + 1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        check_for_three_consecutive_numbers(n)
