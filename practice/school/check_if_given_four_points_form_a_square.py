"""
Given coordinates of four points in a plane, find if the four points form a square or not.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains 4 space separated integer points a , b , c , d

Output:
For each test case print 1 if the four points form a square else print 0.
Remember to output the answer of each test case in a new line.

Constraints:
1<=T<=100
1<=a,b,c,d<=100

Example:

Input:
2
20 20 20 10 10 20 10 10
10 10 10 10 20 10 20 30

Output:
1
0
"""


def check_if_given_points_form_a_square(arr):
    brr = set(arr)
    if len(brr) == 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = [int(i) for i in input().split()][0:8]
        print(check_if_given_points_form_a_square(arr))
