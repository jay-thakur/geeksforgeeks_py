"""
Midori like chocolates and he loves to try different ones. There are N shops in a market labelled from 1 to N and each shop offers a different variety of chocolate. Midori starts from ith shop and goes ahead to each and every shop. But as there are too many shops Midori would like to know how many more shops he has to visit. You have been given L denoting number of bits required to represent N. You need to print the maximum number of shops he can visit.

Input:

The first line of the input contains T denoting number of test cases.

First line of each test case contains two integers,i and L.


Output:

You need to print the required answer in a new line.
Constraints:



1<=T<=10

1<=i<=N

1<=L<=30


Example:

Sample Input:

1
2 3

Sample Output:

6
"""


def midori_and_chocolates(i, l):
    return (1 << l) - i


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        i, l = [int(i) for i in input().split()][0:2]
        print(midori_and_chocolates(i, l))
