"""
Given a number n, the task is to check whether it can be expressed as a sum of two or more consecutive numbers or not.

Examples:

Input  : n = 10
Output : 1
It can be expressed as sum of two consecutive
numbers 1 + 2 + 3 + 4.

Input  : n = 16
Output : 0
It cannot be expressed as sum of two consecutive
numbers.

Input  : n = 5
Output : 1
2 + 3 = 5

Input:

The first line contains 'T' denoting the number of test cases. Then follows description of test cases.
Each test case contains a single positive integer n.

Output:
Print "1" if number can be expressed as sum of consecutives else "0". (Without the double quotes)


Constraints:
1<=T<=200
0<=N<=10^18

Example:
Input :
2
4
5

Output :
0
1
"""


def sum_of_consecutives(n):
    if n & n - 1 == 0:
        return '0'
    else:
        return '1'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_consecutives(n))
