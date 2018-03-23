"""
Given a 2D matrix, the task is to find maximum sum of a hour glass.

An hour glass is made of 7 cells
in following form.
    A B C
      D
    E F G
Examples:

Input : 1 1 1 0 0
        0 1 0 0 0
        1 1 3 0 0
        0 0 0 2 0
        0 0 0 0 4
Output : 9
Below is the hour glass with
maximum sum:
3 0 0
  2
0 0 4


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two space separated integers N and M denoting the size of the matrix. Then in the next line are N*M values of the matrix (m).

Output:
For each test case in a new line print the required output.

Constraints:
1<=T<=100
1<=N,M<=20
1<=m[][]<1000

Example:
Input:
2
1 2
1 2
3 3
1 1 1 1 1 1 1 1 1

Output:
-1
7
"""


def find_max_sum(arr, n, m):
    if n < 3 or m < 3:
        return -1
    else:
        max_sum = -1
        for i in range(n-2):
            for j in range(m-2):
                s = sum(arr[m * i + j:m * i + j + 3]) + arr[m * (i + 1) + j + 1] + sum(arr[m * (i + 2) + j:m * (i + 2) + j + 3])
                max_sum = max(s, max_sum)

        return max_sum;


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n*m]
        print(find_max_sum(arr, n, m))
