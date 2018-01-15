"""
Write a program to calculate the total surface area and volume of cuboid.

Input:

The first line of the input contains T denoting the number of testcases. Each of the next T lines contains three space
separated positive integers L, B, H denoting the length, width and height of cuboid respectively.

Output:

For each testcase, output two space separated integers denoting surface area and volume of cuboid respectively.

Constraints:

1<=T<=100
1<=l,b,h<=1000

Example:

Input:
1
1 2 3

Output:
22 6
"""


def surface_area_of_cuboid(l, b, h):
    return 2*(l*b + b*h + h*l)


def volume_of_cuboid(l, b, h):
    return l*b*h


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        l, b, h = map(int, input().split())
        print(surface_area_of_cuboid(l, b, h), volume_of_cuboid(l, b, h))