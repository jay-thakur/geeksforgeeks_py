"""
Find the focal length of the spherical mirror with the given radius-of-curvature R.

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each test case contains two lines of input:-
Type of mirror
Radius of curvature R

Output:

For each testcase, print the floor of the focal length.

Constraints:
1<=T<=100
1<=R<=100

Example:

Input:
2
convex
67.67
concave
3.31

Output:
-34
1
"""


def focal_length_of_a_spherical_mirror(str, r):
    if type == "concave":
        return int(r // 2)
    else:
        f = -1 * (r / 2)
        return int(f // 1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        type = input()
        r = float(input())
        print(focal_length_of_a_spherical_mirror(type, r))
