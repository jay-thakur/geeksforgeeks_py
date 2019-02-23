"""
Given a 2-D array of order NxN, swap the values of the triangle above the diagonal with the values of the triangle below it like a mirror image swap. Print the 2-D array obtained in matrix layout. Let the elements of the 2-D array be denoted by A[ i ][ j ], where i, j vary from 0 to N-1.

Input:
First line of input is an integer T, denoting the number of test cases. For each test case, first line of input is
an integer N, denoting order of square matrix. Next line consists of NxN elements of the matrix, separated by a space.

Output:
For each test case, output the resultant matrix in the next line.

Constraints:
1<= T <= 40
1<= N < 50
0<= A[ i ][ j ] < 50

Example:
Input:
1
3
1 2 4 5 9 0 3 1 7

Output:
1 5 3 2 9 1 4 0 7

Explanation:
Elements above the diagonal are swapped with the elements below the diagonal like mirror image swap, treating diagonal
as the mirror and keeping it's elements unchanged.
"""


def swapping_triangles(arr, size):
    res = []
    for i in range(size):
        for j in range(size):
            res.append(arr[j * size + i])
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size * size]
        print(*swapping_triangles(arr, size))
