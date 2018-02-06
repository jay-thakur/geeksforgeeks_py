"""
Write a program to reverse digits of a number.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print the reverse digit of a N digit number.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000000000

Example:

Input:
2
200
122

Output:
2
221
"""


def reverse_digit(n):
    reverse = 0
    while n > 0:
        rem = n % 10;
        reverse = reverse * 10 + rem;
        n = n // 10;
    return reverse

# def reverse_digit(n):
#     return n[::-1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input()) # n = input()
        print(reverse_digit(n))