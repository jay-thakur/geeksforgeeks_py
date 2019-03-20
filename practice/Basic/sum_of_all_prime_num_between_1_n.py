"""
Given a positive integer N, calculate the sum of all prime numbers between 1 and N(inclusive).

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input containing N.

Output:
For each testcase, in a new line, print the sum of all prime numbers between 1 and N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106

Example:
Input:
2
5
10

Output:
10
17
"""


def sum_of_all_prime_num(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    ans = 0
    for i in range(n + 1):
        if prime[i]:
            ans += i
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_all_prime_num(n))