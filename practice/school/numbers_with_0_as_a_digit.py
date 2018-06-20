"""
Given an integer N. The task is to count the number of integers from 1 to N contains 0’s as a digit.

Input:
The first line consists of an integer T i.e number of test cases. The only line of each test case consists of an integer N.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=n<=10000

Example:
Input:
2
21
101

Output:
2
11
"""


def numbers_with_0_as_a_digit(n):
    count = 0
    for i in range(1, n + 1):
        if '0' in str(i):
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(numbers_with_0_as_a_digit(n))
