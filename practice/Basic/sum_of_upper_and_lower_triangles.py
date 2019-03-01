"""
Given a matrix print the sum of upper and lower triangular elements. Upper Triangle consists of elements on the diagonal and above it. Lower triangle consists of elements on the diagonal and below it.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integer n. The next line contains n*n spaced integers.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=n,a[i][j]<=100

Example:
Input:
1
3
6 5 4 1 2 5 7 9 7

Output:
29 32
"""


def sum_of_upper_and_lower_triangle(arr, size):
    upper_sum = 0
    lower_sum = 0
    for i in range(size):
        for j in range(size):
            if j >= i:
                upper_sum += arr[j + i * size]
            if j <= i:
                lower_sum += arr[j + i * size]
    return upper_sum, lower_sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size*size]
        print(*sum_of_upper_and_lower_triangle(arr, size))
