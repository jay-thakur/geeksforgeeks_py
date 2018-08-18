"""
You are given an equation of the form x1+x2+...+xN=K. You need to find the total number of positive integral solutions of this equation.

Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test case follows. Each testcase contains a single line that denotes the equation.

Output:

Print the total number of positive integral solutions.

Constraints:
1<=T<=100
1<=K<=25
2<=N<=10

Example:

Input:
4
a+b=5
a+b=1
a+b+c=10
a+b+c+d+e=15

Output:
4
0
36
1001
"""


def fact(n):
    r = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            r = r * i
        return r


def num_of_positive_integral_sol(s):
    l = s.split('+')
    m = s.split('=')
    n = len(l)
    k = int(m[len(m) - 1])
    if k == 1 or k == 0:
        res = 0
    else:
        res = int(fact(k - 1) / (fact(n - 1) * fact(k - n)))
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(num_of_positive_integral_sol(s))
