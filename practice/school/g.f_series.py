"""
Siddhant made a special series and named it as G.F Series.The series follows this trend  Tn=(Tn-2)2-(Tn-1)  in which the first and the second term are 0 and 1 respectively.Help Siddhant to find  upto N terms of the series .

Input:

First line contain M number of test cases.

Second line contain N upto which series will run.

Output:

Print all the terms which will occur in the series(upto N).
Constraints:
1<=T<=100
1<=N<15
Example:

INPUT:

5
3
4
6
1
2

OUTPUT:

0 1 -1
0 1 -1 2
0 1 -1 2 -1 5
0
0 1
"""


def g_f_series(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return g_f_series(n - 2) * g_f_series(n - 2) - g_f_series(n - 1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        for i in range(1, n + 1):
            print(g_f_series(i), end=" ")
        print()
