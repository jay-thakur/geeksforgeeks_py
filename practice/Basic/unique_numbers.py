"""
In given range, print all numbers having unique digits. e.g. In range 1 to 20 should print all numbers except 11.

Input:
First line consists of T test cases.
The only line of every test case consists of two integers m and n separated by a space.

Output:
For each test case print all unique numbers separated by space.

Constraints:
1<=T<=100
1<=m,n<1000

Example:
Input:
1
10 20
Output:
10 12 13 14 15 16 17 18 19 20
"""


def unique_number(a, b):
    res = []
    for j in range(a, b + 1):
        j = str(j)
        if len(j) == len(set(j)):
            res.append(j)
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()][0:2]
        print(*unique_number(a, b))
