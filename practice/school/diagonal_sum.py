"""
Given a square matrix of size M×M . Your task is to calculate the sum of its diagonals.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. First line of each test case contains a single integer M denoting the size of the square matrix. The next  line contains M*M space separated values of the matrix A.

Output:
For each test case in a new line print the sum of diagonals of the matrix.

Constraints:
1 ≤ T ≤ 20
2 ≤ N ≤ 10
1 ≤ A[i] ≤ 20

Example:

Input:

1
3
1 1 1 1 1 1 1 1 1

Output:
6
"""


def diagonal_sum(arr, m):
    sum = 0
    for i in range(0, m):
        sum = sum + arr[i * m + i] + arr[i * m + m - 1 - i]
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m = int(input())
        arr = [int(i) for i in input().split()][0:m * m]
        print(diagonal_sum(arr, m))
