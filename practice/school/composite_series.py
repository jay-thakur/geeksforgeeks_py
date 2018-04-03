"""

Given a number N, print all the composite numbers less than or equal to N. The number should be printed in ascending order.

Input:
The first line contain an Integer T denoting the number of  test cases . Then T test cases follow. Each test case consist of an single integer N.

Output:
Print all the composite Number form 0 to N.

Constraints:

1 ≤ T ≤ 50
4 ≤ N ≤ 10000

Example:
Input:
2
10
6
Output:
4 6 8 9 10
4 6
"""


def composite_series(n):
    for i in range(4, n + 1):
        for j in range(2, i):
            if i % j == 0:
                print(i, end=' ')
                break
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        composite_series(n)
