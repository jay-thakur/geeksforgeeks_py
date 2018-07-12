"""
Chunky gets happy by eating Melody.
Given an array of N elements each element represent happiness chunky get by eating melody.
Chunky knows why melody is so chocolaty but will only tell you once you tell him the Max happiness he can get by eating two adjacent melodies.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an integer N and the second line contains N space separated array elements.

Output:
For each test case, print the Maximum Happiness in new line.

Constraints:
1 <= T <= 100
1 <= N <= 100000
-100000 <= A[i] <= 100000


Example:

Input:
2
5
1 2 3 4 5
4
5 2 3 4

Output:
9
7
"""


def why_so_chocolate(arr, size):
    i = 0
    max = arr[i] + arr[i + 1]
    for i in range(0, size - 1):
        if arr[i] + arr[i + 1] > max:
            max = arr[i] + arr[i + 1]
        i = i + 1
    return max


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(why_so_chocolate(arr, size))
