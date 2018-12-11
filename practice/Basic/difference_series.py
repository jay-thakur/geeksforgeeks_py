"""
Given a series of numbers  3,10,21,36 …., and series starting from n=1 , find the pattern and output the nth value of above series.

Input:
The first line of the input contains a single integer T denoting the number of test cases.
The first line of each test case contains n.

Output:
For each test case, output the nth value of above series.

Constraints:
1 ≤ T ≤ 100
1 ≤ n≤ 100

Example:
Input:

4
1
2
3
4

Output:
3
10
21
36
"""


def difference_series(n):
    return n * (2 * n + 1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(difference_series(n))
