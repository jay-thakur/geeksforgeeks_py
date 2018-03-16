"""
Given a date, the task is to check if it is valid or not. It may be assumed that the given date is in range from 01/01/1800 to 31/12/9999 and any date not within this range will also be considered invalid.

Examples :

Input : d = 10, m = 12, y = 2000
Output : 1
The given date 10/12/2000 is valid

Input  : d = 30, m = 2, y = 2000
Output : 0
The given date 30/2/2000 is invalid. The
February month cannot have 30 as day.


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 space separated integers d, m, y denoting the day, month and the year respectively.

Output:
For each test case in a new line print 1 if the date is a valid date else print 0.

Constraints:
1<=T<=100
1<=d, m, y<=10000

Example:
Input:
2
10 12 2000
30 2 2000
Output:
1
0
"""

import calendar as cl


def is_valid_date(d, m, y):
    if y > 9999 or y < 1800:
        return False
    if m < 1 or m > 12:
        return False
    if d < 1 or d > 31:
        return False

    if m == 2:
        if cl.isleap(y):
            return d <= 29
        else:
            return d <= 28

    if m == 4 or m == 6 or m == 9 or m == 11:
        return d <= 30

    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().split(" ")
        day = int(arr[0])
        month = int(arr[1])
        year = int(arr[2])

        print('1' if is_valid_date(day, month, year) else '0')

