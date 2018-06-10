"""
Given an integer n, you need to print the following pattern pattern.

n=4
      Output :
       4444444
       4333334
       4322234
       4321234
       4322234
       4333334
       4444444

n=3
        Output :
         33333
         32223
         32123
         32223
         33333


Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each test case contains one lines of input denoting the value of n.

Output:
For each test case, Print the mentioned pattern.

Constraints:
1<=T<=100
1<=N<=9

Example:

Input:
2
3
4

Output:
33333
32223
32123
33333
4444444
4333334
4322234
4321234
4322234
4333334
4444444
"""


def print_pattern(n):
    for j in range(1, n * 2):
        for k in range(1, n * 2):
            print(max(abs(n - j), abs(n - k)) + 1, end="")
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print_pattern(n)
