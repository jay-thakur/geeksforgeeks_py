"""
Write a program to find transpose of a square matrix of size N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the square matrix. Then in the next line are N*N space separated values of the matrix.

Output:
For each test case output will be the space separated values of the transpose of the matrix


Constraints:
1<=T<=1000
1<=N<=20

Example:
Input:
2
4
1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4
2
1 2 -9 -2


Output:
1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4
1 -9 2 -2
"""


def transpose_matrix(matrix, size):
    return [matrix[j * size + i] for i in range(size) for j in range(size)]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        matrix = [int(i) for i in input().split()][0:size*size]
        print(*transpose_matrix(matrix, size))
