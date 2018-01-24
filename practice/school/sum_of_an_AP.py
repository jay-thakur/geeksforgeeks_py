"""
Write a program to print sum of an AP with n terms with first term a and common difference d.

Input:

The first line of the input contains T denoting the number of testcases. The first line of the test case will be the number of terms of AP and second line its first term and common difference.
Output:

For each test case, output will be the sum of AP
Constraints:

1 <= T<= 100

1 <= N <= 1000

1 <= a,d <= 100


Example:

Input:

1
5
1 3

Output:

35
"""


def sum_of_an_AP(a, d):
    return int((n * (2*a + (n-1)*d)/2))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a, d = map(int, input().split())
        print(sum_of_an_AP(a, d))