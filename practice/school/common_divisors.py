"""
Given two integer numbers, the task is to find count of all common divisors of given numbers?

Input : a = 12, b = 24
Output: 6
// all common divisors are 1, 2, 3,
// 4, 6 and 12

Input : a = 3, b = 17
Output: 1
// all common divisors are 1

Input : a = 20, b = 36
Output: 3
// all common divisors are 1, 2, 4
Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of one line only. The line consists one two space separated positive integers which denote a and b.


Output:

Corresponding to each test case, in a new line, print the number of common divisors.


Constraints:

1 ≤ T ≤ 200

1 ≤ a, b ≤ 10000


Example:

Input

2
232 8
1 354

Output

4
1
"""


def common_divisors(a, b):
    m = min(a, b)
    count = 0
    for i in range(1, m + 1):
        if a % i == 0 and b % i == 0:
            count = count + 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(common_divisors(a, b))