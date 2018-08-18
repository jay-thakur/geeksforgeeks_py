"""
Given a number N. check whether a given number N  is palindrome or not in it's both formates (Decimal and Binary ).

Input:

The first line of the input contains T i.e number of test cases. Each line of the test case contains a number  N.

Output:

For each test Case, you have to Print "Yes" or "No" if given number is palindrome   Print "Yes" else "No".

Constraints:

1<=T<=1000

0<=N < 10^5

Example:

Input:
3
1
12
7

Output:
Yes
No
Yes

Explanation:
Test case 3: 7 is palindrome in it's decimal and also in it's binary (111)  : output is "Yes "
"""


def palindrome_in_both_decimal_and_binary(n):
    b = bin(int(n))[2:]
    if n == n[::-1] and b == b[::-1]:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(palindrome_in_both_decimal_and_binary(n))
