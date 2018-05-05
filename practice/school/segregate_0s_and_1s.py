"""
You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input C[i].

Output:
Print 0s on left side and 1s on right side.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 500
0 ≤ C[i] ≤ 1

Example:

Input:

2
5
0 0 1 1 0
4
1 1 1 1

Output:

0 0 0 1 1

1 1 1 1
"""


def segregate_0_and_1(arr):
    arr.sort()
    return arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*segregate_0_and_1(arr), end=' ')
        print()
