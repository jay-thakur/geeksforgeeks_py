"""
A given series 3, 5, 9, ........11, 15, ...........21,...... and so on. You need to identify the pattern and determine whether the input number  ( n ) is a part of the given series or not.

Input:
The first line of the input contains a single integer T denoting the number of test cases.
The first line of each test case contains n.

Output:
For each test case, Print Yes if n is a part of the given series or else No.

Constraints:
1 <= T <= 200
1 <= n <= 1000

Example:
Input:
6
917
101
901
51
102
893
Output:
Yes
Yes
No
Yes
No
No
"""


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "No"
            break
    else:
        return "Yes"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        n = n + 2
        print(is_prime(n))
