"""
Given two integer number n and d. The task is to find the number between 0 to n which contain the specific digit d.

Input:
The first line contains an integer T, the number of test cases. For each test case, there are two integer n & d.

Output:
For each test case, the output is the numbers that contain the integer d. Print "-1" if no such number found.

Constraints:
1<=T<=100
0<=n<=10^3​
0<=d<=9

Example:
Input
2
20 5
50 2
Output
5 15​
2 12 20 21 22 23 24 25 26 27 28 29 32 42
"""


def find_the_num(n, x):
    c = 0
    for i in range(n + 1):
        if str(x) in str(i):
            print(i, end=' ')
            c += 1

    if c == 0:
        print(-1)
    else:
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = [int(i) for i in input().split()][0:2]
        find_the_num(n, x)
