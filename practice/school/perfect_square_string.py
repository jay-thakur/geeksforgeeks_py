"""
*School Problem's Submission isn't counted in score!

You are given a string S. Your task is to determine if sum of ASCII values of all character results in a perfect square or not.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has a string S

Output:
Print 1 if the resulting sum is a perfect square, else print 0.

Constraints:
1<=T<=100
1<=|S|<=1000

Example:

Input:
4
1Qy
abcd
efgh
d

Output:
0
0
0
1
"""


def perfect_square_string(str):
    s = sum(map(ord, str))
    if int(s ** 0.5) ** 2 == s:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(perfect_square_string(str))
