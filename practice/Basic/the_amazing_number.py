"""
You are given a number N. Your task is to determine if N is an amazing number or not.  A number is called amazing if it has exactly three distinct divisors.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains a single line having N as input.

Output:
For each testcase, print 1 if the number is amazing, else print 0.

Constraints:
1<=T<=1112
2<=N<=1018

Example:

Input:
3
2
3
4

Output:
0
0
1

Explanation:

For testcase 1: 2 has the following divisors: 1, 2. Only 2 divisors, so we print 0.
For testcase 2: 3 has the following divisors: 1, 3. Only 2 divisors, so we print 0.
For testcase 3: 4 has the following divisors: 1, 2,4. Exactly 3 divisors, so we print 1.
"""


import math


def the_amazing_number(num):
    sqrt = int(math.sqrt(num))
    if sqrt * sqrt == num:
        ok = 1
        if sqrt is not 2 and sqrt % 2 == 0:
            ok = 0
        else:
            for x in range(3, int(math.sqrt(sqrt)) + 1, 2):
                if sqrt % x == 0:
                    ok = 0
                    break
        return ok
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num = int(input())
        print(the_amazing_number(num))
