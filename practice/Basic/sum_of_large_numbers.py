"""
A pair of two very large positive integers is given. The task is to print their sum.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. In the first line is the first number A and in the second is the second number B.

Output:
Corresponding to each test case, print the sum of A and B in a new line.

Constraints:
1 ≤ T ≤ 100
1 ≤ A,B ≤ 101002

Example:

Input
2
63457
645
9999788586376
123456789

Output
64102
9999912043165
"""


def sum_of_large_numbers(n1, n2):
    return n1 + n2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n1 = int(input())
        n2 = int(input())
        print(sum_of_large_numbers(n1, n2))
