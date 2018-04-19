"""
Given coordinates of 2 points on a cartesian plane, output the distance between them rounded up to nearest integer.

Input:
The first line of the input contains the number of test cases T. Each line contains 4 integers denoting those 2 points as (x1,y1), (x2,y2).

Output:
For each test case print in a single line the distance between the two points.

Constraints:
1<=T<=100
-1000000<=|x1,x2,y1,y2|<=1000000


Example:
Input:
4
0 0 2 -2
-20 23 -15 68
30 37 79 -51
-69 63 57 11

Output:
3
45
101
136
"""


def distance_between_2_points(x1, y1, x2, y2):
    result = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return round(result)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        x1, y1, x2, y2 = [int(i) for i in input().split()][0:4]
        print(distance_between_2_points(x1, y1, x2, y2))
