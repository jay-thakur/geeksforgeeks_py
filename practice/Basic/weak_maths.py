"""
Raj wants to buy an array of integers. As you know nothing is free these days, so to buy the array Raj needs to pay amount equal to lowest integer with a and b as their divisors. Here a and b are the minimum and maximum of the given array respectively. As Raj is weak at mathematics help him to find the cost he needs to pay.

Input:

First line of each test case contains an integer T, denoting number of test cases. First line of each test case contains an integer N, denoting the size of the array. Second line of each test case contains N space separated integers denoting the elements of the array.

Output:

For each test case print the amount Raj needs to pay in separate lines.

Constraints:

1<=T<=10

1<=N<=10^5

1<=A[i]<=10^5

A[i] represents the ith element of the array.

Sample Input:

2
4
3 5 8 6
4
1 2 8 6
Sample Output:

24

8
"""
import math


def weak_maths(arr):
    n1, n2 = max(arr), min(arr)
    res = (n1 * n2) / math.gcd(n1, n2)
    return int(res)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(weak_maths(arr))
