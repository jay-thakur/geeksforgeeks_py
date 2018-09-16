"""
You are a human of height 2 meters. You are standing at some distance from a tower. You have a device that is a little bit faulty. At a time, it can either measure your distance from the tower (d), or it can measure the height of the tower (h). Other than that, it can measure the angle of elevation of the tower's top from your eye level. You need to find the variable that is unavailable. That is, if you know the distance, you need to find the height; if you know the height, you need to find the distance.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase contains a single line of input. The single line of input contains three things separated by spaces: The type, the value of that type, the angle. See examples for more clarification.

Output:
Print the floor of the answer.

Constraints:
1<=T<=100
Type={h,d}
10<=h,d<=1000
4<=angle<=89

Example:

Input:
3
d 12 67
h 100 66
h 67 67

Output:
30
43
27

Note: The angle is in degrees. The distances are in meters. If required, use PI=3.14

Explanation:
For first testcase: The type is d, that means, we are given the distance from the tower. The value of d is 12.
The angle given is 67 degrees. We need to find h in this case. The value of h that we get after floor is 30
"""


import math


def human_and_the_tower(type, d, angle):
    d = int(d)
    angle = int(angle)
    tan = (math.tan(angle * 3.14 / 180))
    if type == 'h':
        return int((d - 2) / tan)
    else:
        return int(2 + tan * d)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        type, d, angle = [i for i in input().split()][0:3]
        print(human_and_the_tower(type, d, angle))
