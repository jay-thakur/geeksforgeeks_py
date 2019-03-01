"""
Given a series as shown below:

               1  2
            3  4  5  6
        7  8  9 10 11 12
 13 14 15 16 17 18 19 20
    ..........................
    ............................
             (so on)

You are given a number N, you need to write a program to find the sum of all elements in the N-th row of above series.

Input:
First line of input contains a single integer T which denotes the number of test cases. First line of each test case contains a single intger N.

Output:
For each test case, print the sum of all the elements present in Nth row of above series.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
2
4
Output:
18
132
"""


def sum_terms_nth_row(n):
    count = 0
    a = n * (n - 1) + 1
    b = n * (n + 1)
    for x in range(a, b + 1):
        count += x
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_terms_nth_row(n))
