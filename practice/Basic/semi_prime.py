"""
Given a positive integer n. Find whether a number is a semiprime or not. Print True if number is semiprime else False. A semiprime is a natural number that is a product of two prime numbers .

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.


Output:
Print 'True' if it is semi prime,otherwise print 'False'.


Constraints:

1<=T<=100

1<=N<=100000
Example:

Input:
2
6
8

Output:
True
False

Explanation:
Testcase 1 : N=6, True
6 is a semiprime number as it is a product of two prime numbers 2 and 3.

Testcase 2: N = 8 , False
"""


def semi_prime(n):
    c = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            c = c + 1
    if c == 2:
        return 'True'
    else:
        return 'False'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(semi_prime(n))