"""
Given a matrix M[][], the task is to check if the sum of i-th row is equal to the sum of i-th column or not.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains two integers R and C and the second line contains R*C space separated matrix elements.

Output:
For each test case, if sums are equal for one or more rows and column, print "Yes" else print "No".

Constraints:
1<=T<=100
1<=R,C<=500
0<=M[][]<=103

Example:
Input:
2
4 4
1 2 3 4 9 5 3 1 0 3 5 6 0 4 5 6
3 3
1 2 3 1 2 3 1 1 3

Output:
Yes
No
"""


def sum_of_row_col(arr, r, c):
    l1 = []
    for i in range(0, r * c, c):
        l1.append(arr[i:i + c])
    a = 0
    for i in range(0, r):
        row_sum = sum(l1[i])
        col_sum = 0
        for j in range(0, r):
            if i < c:
                col_sum += l1[j][i]
        if row_sum == col_sum:
            a = 1
            break
    return "Yes" if a == 1 else "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        r, c = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:r * c]
        print(sum_of_row_col(arr, r, c))
