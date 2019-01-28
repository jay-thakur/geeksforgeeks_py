"""
Given two arrays A and B, find union between these two array.  If there are repetitions, then only one occurrence of element should be printed in union.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consist of three lines.
The first line of each test case contains two space separated integers N and M, where N is the size of array A and M is the size of array B.
The second line of each test case contains N space separated integers denoting elements of array A.
The third line of each test case contains M space separated integers denoting elements of array B.

Output:

Correspoding to each test case, print in a new line, the union of the two arrays in sorted order.

Constraints:

1 ≤ T ≤ 30
1 ≤ N, M ≤ 1000
1 ≤ A[i], B[i] < 1000

Example:

Input:
2
5 3
1 2 3 4 5
1 2 3
6 2
85 25 1 32 54 6
85 2

Output:
1 2 3 4 5
1 2 6 25 32 54 85
"""


def union_of_two_arrays(arr_A, arr_B):
    arr_A.extend(arr_B)
    return set(arr_A)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        arr_A = [int(i) for i in input().split()][0:n]
        arr_B = [int(i) for i in input().split()][0:m]
        print(*union_of_two_arrays(arr_A, arr_B))
