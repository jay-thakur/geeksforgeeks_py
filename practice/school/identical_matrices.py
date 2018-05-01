"""
Write a program to check whether two matrices are identical or not.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test contains an integer N denoting the size of the square matrix. Then the two square matrix of size N*N is taken as input with space separating integers.

Output:
Print "Yes" (without quotes) if matrices are identical and "No" if not identical.

Constraints:
1<=T<=1000
1<=N<=20
1<=a[i][j]<=1000
1<=b[i][j]<=1000

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
Yes
No
"""


def identical_matrix(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2):
        for i in range(len(matrix_1)):
            if matrix_1[i] != matrix_2[i]:
                return 'No'
                break
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        matrix_1 = [int(i) for i in input().split()][0:size*size]
        matrix_2 = [int(i) for i in input().split()][0:size*size]
        print(identical_matrix(matrix_1, matrix_2))
