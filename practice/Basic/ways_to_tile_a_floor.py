"""
Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1, write code to find the number of ways the floor can be tiled. A tile can either be placed horizontally i.e as a 1 x 2 tile or vertically i.e as 2 x 1 tile.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is W.

Output:

Print number of ways the floor can be tiled in a separate line.

Constraints:

1 ≤ T ≤ 50
1 ≤ W ≤ 70

Example:

Input
2
5
3

Output
8
3
"""


def ways_to_tile_a_floor(n):
    a, b, c = 1, 1, 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(ways_to_tile_a_floor(n))
