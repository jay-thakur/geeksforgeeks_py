"""
Determine the row index with minimum number of ones. The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise . If two or more rows have same number of 1's than print the row with smallest index.

Note: If there is no '1' in any of the row than print '-1'.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of two integer n and m. The next line consists of n*m spaced integers.

Output:
Print the index of the row with minimum number of 1's.

Constraints:
1<=T<=200
1<=n,m<=100

Example:
Input:
2
3 3
0 0 0 0 0 0 0 0 0
4 4
0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1

Output:
-1
0
"""


def row_of_min_1s(matrix, n, m):
    r = [None] * n

    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[i * m + j] == 1:
                count += 1
        r[i] = count

    if sum(r) == 0:
        return -1
    else:
        mi = min(i for i in r if i > 0)
        for i in range(len(r)):
            if r[i] == mi:
                return i
                break


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        matrix = [int(i) for i in input().split()][0:n * m]
        print(row_of_min_1s(matrix, n, m))
