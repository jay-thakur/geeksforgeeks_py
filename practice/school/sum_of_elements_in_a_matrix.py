"""
Given a non null integer matrix,calculate the sum of its elements.

Input: First line contains T , the number of test cases.First line of each test contains 2 integers N,M and N lines follow which contain M spaced integers.

Output:Single line for each test case containing the sum

Constraints: 1<= N,M<=10 , elements of matrix   -1000<=matrix<=1000

Example:
Input:
1
2 3
1 0 0
8 -9 -1

Output

-1
"""


def matrix_sum(matrix):
    return sum(matrix)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        row, col = [int(i) for i in input().split()][0:2]

        matrix = [int(j) for j in input().split()][0:row * col]

        print(matrix_sum(matrix))
