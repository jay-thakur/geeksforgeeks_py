"""
Stuti is a very good dancer. She is preparing for her performance at her college fest. But unfortunately she has to submit her maths assignment just before the college fest. She has completed most of the problems but she is stuck at one. She has no clue how to solve this problem. Now she is in a dilemma of whether to prepare for her performance or try to solve that problem. She is very tensed. She needs your help to solve this problem.

Problem contains a number N(1<= N <= 1000000000). If this number is the sum of first 's' natural number then print 's' otherwise print -1.

INPUT
First line denotes the number of test cases(1<= T <= 100).

And next T lines contains a single integer.

OUTPUT
For each test case print a single integer in next line.

Sample Input:
2
10
17
Sample Output:
4
-1
"""
import math


def stuti_and_her_problem(n):
    ans = (math.sqrt(1 + 8 * n) - 1) / 2
    if int(ans) == math.ceil(ans):
        return int(ans)
    else:
        return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(stuti_and_her_problem(n))
