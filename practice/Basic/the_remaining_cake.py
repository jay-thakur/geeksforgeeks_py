"""
Given a circular cake of radius R, divide the cake amongst N number of people such that every person gets 1/Mth posrtion of the cake, where N and M are positive non-zero integers and M>=N. Find the arc length of the piece of cake that is left over after the distribution.

Input:

First line of input is an integer T, denoting the number of test cases. For each test case, input three values separated by a space on a single line, R, N and M, denoting radius of cake, number of people and fraction of share to be given to each person respectively. R is a floating point number with a precision of 2. For each test case, M is always greater than or equal to N.

Output:

Output of each test case gives a floating point number upto a precision of 2 digits, denoting the arc length of the remaining cake.

Constraints:

0.00<=R<10.00
1<=N<=20
1<=M<=30
PI = 3.14


Example:

Input:

4
7.50 4 7
6.66 3 4
3.80 4 5
8.00 5 5

Output:

20.19
10.46
4.77
0.00

Explanation:

In the first test case, 4 people must be given 1/7th share of the circular cake.
Hence 4/7th portion of the cake is taken away. The remaining 3/7th portion's arc length is calculated to be 20.19 units.

Similarly, for the rest three test cases, the arc length of the remaining portion is calculated using the necessary
arithmetic and mathematical operations.
"""


def the_remaining_cake(arr):
    R = float(arr[0])
    N = int(arr[1])
    M = int(arr[2])

    op = 2 * 3.14 * R * ((M - N) / M)
    op += 0.00001

    return round(op, 2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = [i for i in input().split()][0:3]
        print(the_remaining_cake(arr))
