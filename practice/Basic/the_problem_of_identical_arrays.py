"""
Two arrays of size N are called identical arrays if they contain the same elements. The order of elements in both arrays could be different; however, both the arrays must contain same elements. You are given two arrays of size N.

You need to determine if the arrays are identical or not.

Input:
The first line of the input contains a single integer T, denoting the number oftest cases. Then T test case follows. Each test case contains 3 lines:-
size of array N
elements of array1
elements of array2

Output:
Print 1 if the arrays are identical, and print 0 if they are not identical.

Constraints:
1<=T<=100
1<=N<=1000
0<=A[i]<=9

Example:

Input:
3
5
1 2 3 4 5
3 4 1 2 5
4
1 2 3 4
1 2 3 9
1
8
8

Output:
1
0
1
"""


def identical_arrays(arr, brr):
    arr.sort()
    brr.sort()
    if arr == brr:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        brr = [int(i) for i in input().split()][0:size]

        print(identical_arrays(arr, brr))
