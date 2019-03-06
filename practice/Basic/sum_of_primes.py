"""
Your task is to calculate sum  of primes present as digits of given number N.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The next T lines contains an integer N.

Output:
Print sum of primes in the digit

Constraints:
1 ≤ T ≤ 50
2 ≤ N ≤ 50000


Example:

Input:

2
333
686

Output:
9
0
"""


def sum_of_primes(n):
    p = "2357"
    s = 0
    for i in range(len(n)):
        if n[i] in p:
            s = s + int(n[i])
    return s


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(sum_of_primes(n))
