"""
Given two force vectors, find out whether they are parallel, perpendicular or neither. Let the first vector be A = a1 i +a2 j + a3 k and the second vector be B = b1 i + b2 j + b3 k.

A.B = a1*b1 + a2*b2 + a3*b3

A x B = (a2*b3 - a3*b2) i - (a1*b3 - b1*a3) j + (a1*b2 - a2*b1) k

|A|^2 = a1^2 + a2^2 + a3^2

If A.B = 0, then A and B are perpendicular.

If |A X B|^2 = 0, then A and B are parallel.

Input:

The first line of input takes the number of test cases, T. Then T test cases follow. Each test case has 2 input lines.The first line of each test case takes 3 space separated integers representing the components of the first force vector in x, y and z directions. The second line of each test case takes 3 space separated integers representing the components of the second force vector in x, y and z directions.

Output:

Print 1 if the 2 vectors are parallel, 2 in case they are perpendicular, 0 otherwise.

Constraints:

1<=T<=100

-100<=Component<=100

Example:

Input:
3
3 2 1
6 4 2
4 6 1
1 -1 2
10 9 5
2 6 1

Output:
1
2
0
"""
import math


def perpendicular(a1, a2, a3, b1, b2, b3):
    return a1 * b1 + a2 * b2 + a3 * b3


def parallel(a1, a2, a3, b1, b2, b3):
    return (a2 * b3 - a3 * b2) - (a1 * b3 - b1 * a3) + (a1 * b2 - a2 * b1)


def parallel_or_perpendicular(a1, a2, a3, b1, b2, b3):
    ab = perpendicular(a1, a2, a3, b1, b2, b3)
    axb = parallel(a1, a2, a3, b1, b2, b3)

    if ab == 0:
        return 2
    elif math.pow(axb, 2) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a1, a2, a3 = [int(i) for i in input().split()][0:3]
        b1, b2, b3 = [int(i) for i in input().split()][0:3]

        print(parallel_or_perpendicular(a1, a2, a3, b1, b2, b3))
