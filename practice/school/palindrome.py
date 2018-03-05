"""
Given an integer, check whether it is a palindrome or not.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line. The first line of each test case contains a single integer N to be checked for palindrome.

Output:
Print "Yes" or "No" (without quotes) depending on whether the number is palindrome or not.

Constraints:
1 <= T <= 1000
1 <= N <= 10000

Example:
Input:
3
6
167
55555

Output:
Yes
No
Yes
"""


def is_palindrome(n):
    sum = 0
    temp = n

    while n > 0:
        r = n % 10
        sum = (sum * 10)+r
        n = n // 10;

    return temp == sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print('Yes' if is_palindrome(n) else 'No')