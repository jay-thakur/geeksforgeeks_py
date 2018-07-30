"""
Given an integer n, find the absolute difference between sum of the squares of first n natural numbers and square of sum of first n natural numbers.

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

For each  testcase,  print the absolute difference between sum of the squares of first n natural numbers and square of sum of first n natural numbers.
Constraints:

1<=T<=100

1<=N<=1000
Example:

Input:
2
10
5

Output:
2640
170

Explanation: Testcase 2 : N = 5, Sum of 5 natural numbers from 1 to 5 = 15 i.e. 15 *15 = 225.
Sum of squares of numbers from 1 to 5 = 1 + 4 + 9+ 16+ 25 =  55.
So, absolute difference is (225 - 55) = 170.
"""


def squares_difference(n):
    s1 = (n * (n + 1) * (2 * n + 1)) // 6
    s2 = (n * (n + 1)) // 2
    s2 = s2 * s2
    return abs(s1 - s2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(squares_difference(n))
