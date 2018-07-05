"""
Given a, b and n. Find x and y that satisfies equation ax + by = n.

INPUT : The first line consists of an integer T i.e. the number of test cases. First and last line of each test case consists of three integers a,b and n.

OUTPUT : Print the required values of x and y with a space in between. In case when no X and Y is possible, please output "No solution" (i.e. w/o quotes).

CONSTRAINTS :
1<=T<=100
1<=a,b,n<=104

EXAMPLES:
INPUT:
2
2 3 7
4 2 7

OUTPUT:
2 1
No solution
"""


def find_X_Y(a, b, n):
    flag = 0
    for x in range(n + 1):
        y = (n - a * x) / b
        if y % 1 == 0 and y > 0:
            print(x, int(y))
            flag = 1
    if flag == 0:
        print("No solution")


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b, n = [int(i) for i in input().split()][0:3]
        find_X_Y(a, b, n)
