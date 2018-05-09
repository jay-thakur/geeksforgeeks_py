"""
Find the area of a triangle with all its three sides given as a,b and c.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains
three space-separated integers a,b and c.

Output:
Output the area of the triangle answer with a precision of 6 decimal places.The area is to be printed as 0.000000 if the triangle does not exist.

Constraints:
1<=t<=200
1<=a,b,c <= 100

Example:
Input:
2
2 2 3
3 4 5

Output:
1.984313
6.000000
"""


def area_of_a_triangle(a, b, c):
    s = (a + b + c) / 2
    if (s * (s - a) * (s - b) * (s - c)) < 0:
        return "0.000000"
    else:
        s = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(s, 6)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b, c = [int(i) for i in input().split()][0:3]
        print(area_of_a_triangle(a, b, c))
