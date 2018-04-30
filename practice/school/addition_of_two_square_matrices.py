"""
Write a program to add two matrices.

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test contains an integer N denoting the size of the square matrix. Then the two square matrix of size N*N is taken as input in next two lines.

Output:
For each test case in a new line print separated values of the matrix denoting addition of the two matrices.


Constraints:
1<=T<=100
1<=N<=20
1<=a[i][j]<=1000

Example:
Input:
2
4
1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4
1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4
2
1 2 3 4
3 4 2 1

Output:
2 2 2 2 4 4 4 4 6 6 6 6 8 8 8 8
4 6 5 5
"""


def add_matrix(matrix_1, matrix_2):
    return map(lambda x, y: x + y, matrix_1, matrix_2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        matrix_1 = [int(i) for i in input().split()][0:size * size]
        matrix_2 = [int(i) for i in input().split()][0:size * size]
        print(*add_matrix(matrix_1, matrix_2))
