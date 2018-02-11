"""
Given two dates, find total number of days between them. The count of days must be calculated in O(1) time and O(1) auxiliary space.

Note: The system follows Gregorian calender from the beginning of the time.

Input:

The first line of input contains an integer T denoting the number of test cases.
Each test case consist of two lines each containing three integers D, M and Y, separated with a space, denoting date, month and year respectively.

Output:

Print a single integer denoting total number of days between the given dates.

Constraints:
1 ≤ T ≤ 100
1 ≤ D ≤ 31
1 ≤ M ≤ 12
1 ≤ Y ≤ 3000

Example:

Input
4
10 2 2014
10 3 2015
10 2 2000
10 3 2000
10 2 2000
10 2 2000
1 2 2000
1 2 2004

Output
393
29
0
1461
"""

from datetime import date


def no_of_days_between(date1, date2):
    return abs((date1 - date2).days)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        d1, m1, y1 = map(int, input().split())
        d2, m2, y2 = map(int, input().split())
        date1 = date(y1, m1, d1)
        date2 = date(y2, m2, d2)
        print(no_of_days_between(date1, date2))