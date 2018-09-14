"""
Ishaan is curious about numbers. He takes any 2 random numbers A and B. He wants to find out that whether X can be written as a sum of Y distinct npositive integers.
Help him find out whether it is possible or not.

Input :
First line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains 2 space-separated integers A and B.

Output :
For each test case, print "1" if it is possible, else print "0" (without quotes "").

Constraints :
1 <= T <= 200
1 <= A,B <= 10^5

Example :
Input :
3
5 2
6 2
5 3
Output :
1
1
0

Explaination :
Case 1 :
5 can be written as a sum of 2 numbers : 1+4 or 2+3

Case 2 :
6 can be written as a sum of 2 numbers : 1+5 or 2+4

Case 3 :
5 can't be written as a sum of 3 numbers.
"""


def ishaans_sum_problem(a, b):
    if (b * (b + 1)) // 2 < a:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()][0:2]
        print(ishaans_sum_problem(a, b))
