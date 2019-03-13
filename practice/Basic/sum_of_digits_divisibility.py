"""
Check that the number can be divided by the sum of its digit.

Input:

The first line of input contains an integer T denoting the number of test cases.Then T test cases follow .Each test case consist of an integer N.

Output:

Print 1 if divisible else 0.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 100000

Example:

Input
2
18
19170

Output
1
1
"""


def sum_of_digits_divisibility(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if n % sum == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_digits_divisibility(n))
