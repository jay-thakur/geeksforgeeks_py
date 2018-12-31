"""
Given an integer N, return  count of numbers having odd number of factors from 1 to N inclusive.

Input:
The first line contains T denoting the number of test cases. Then the following T lines contains the single integer N denoting the value of N.

Output:
Output the total number of numbers having odd number of factors.

Constraints:
1<=T<=30
1<=N<=10^9

Example:
Input :
2
1
5

Output :
1
2
"""


def count_odd_factors(n):
    return int(n**0.5)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_odd_factors(n))
