"""
Given the value of n, we need to find the sum of the series where i-th term is sum of first i odd natural numbers.

Note:- Sum of the series 1 + (1+3) + (1+3+5) + (1+3+5+7) + …… + (1+3+5+7+…+(2n-1))

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

Print the sum of the series of N terms for each testcase.
Constraints:

1<=T<=100

1<=N<=1000
Example:

Input:
2
2
5

Output:
5
55

Explanation:
Testcase 1:
(1) + (1+3) = 5
Testcase 2:
(1) + (1+3) + (1+3+5) + (1+3+5+7) + (1+3+5+7+9) = 55
"""


def special_odd_series_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(special_odd_series_sum(n))
