"""
Calculate the area of rectangle, right angled triangle and circle.

Input:

The first line of the input contains T denoting the number of testcases. Then follows the description of testcase. Each testcase contains 5 space separated positive integers denoting the length of rectangle, width of rectangle, base of right angled triangle, perpendicular of right angled triangle and radius of circle respectively.

Output:

For each testcase, output a single line containing 3 space separated integers denoting the area of rectangle, area of right angled triangle, and area of circle respectively.

Note: We need to print the floor values of the areas. Also take value of pi = 3.14

Constraints:

1<=T<=50

1<=length / breadth / base / perpendicular / radius  <= 100

Example:

Input:
1
32 32 54 12 52

Output:
1024 324 8490
"""
import math


def area_of_rectangle(length, width):
    return length * width


def area_of_right_angled_tringle(base, perpendicular):
    return math.floor(0.5 * base * perpendicular)


def area_of_circle(radius):
    return math.floor(3.14 * radius * radius)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        length, width, base, perpendicular, radius = map(int, input().split())
        print(area_of_rectangle(length, width), end=' ')
        print(area_of_right_angled_tringle(base, perpendicular), end=' ')
        print(area_of_circle(radius))
