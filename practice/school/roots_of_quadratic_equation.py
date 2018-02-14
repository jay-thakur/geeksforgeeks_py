"""
Given a quadratic equation in the form ax2 + bx + c, find floor of roots of it.  For example floor of 5.6 is 5.

Input:  First line contains an integer, the number of test cases 'T'. Each test case should contain three positive numbers a,b and c.

Output:  If roots of equations exits, then print the two roots separated by space (Higher valued root should be printed before lower valued). Else if a = 0, then print "Invalid" as equation is not quadratic.  If roots are imaginary, then print "Imaginary"

Constraints:
1<=T<=50
1<=a<=1000
1<=b<=1000
1<=c<=1000


Example:
Input:
3
1 -2 1
1 -7 12
1 4 8

Output:
1 1
4 3
Imaginary
"""
from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        print("Invalid")
    else:
        d = b*b - 4*a*c
        if d < 0:
            print("Imaginary")
        else:
            root1 = int(((-b) + sqrt(d)) // (2 * a))
            root2 = int(((-b) - sqrt(d)) // (2 * a))
            if root1 > root2:
                print(root1, root2)
            else:
                print(root2, root1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b, c = [int(i) for i in input().split()][0:3]
        roots_of_quadratic_equation(a, b, c)