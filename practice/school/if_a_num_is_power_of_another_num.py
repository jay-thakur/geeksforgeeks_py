"""
Given two positive numbers x and y, check if y is a power of x or not.

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain two positive numbers x and y.


Output:
Print 1 if y is a power of x, else print 0.


Constraints:
1<=T<=30
1<=x<=1000
1<=y<=100000000


Example:
Input:
2
2 8
1 3

Output:
1
0

Explanation: 8 is a power of 2, but 3 is not a power of 1.
"""


def is_power(num1, num2):
    if num1 == 1:
        return num2 == 1
    pow_ = 1;
    while pow_ < num2:
        pow_ = pow_ * num1

    return pow_ == num2;


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num1, num2 = [int(i) for i in input().split()][0:2]
        print(1 if is_power(num1, num2) else 0)