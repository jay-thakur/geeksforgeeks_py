"""
Given two strings, the task is to find if a string ('a') can be obtained by rotating another string ('b') by two places.
Examples:

Input : a = "amazon"
        b = "azonam"  // rotated anti-clockwise
Output : 1

Input : a = "amazon"
        b = "onamaz"  // rotated clockwise
Output : 1


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. In the next two line are two string a and b.

Output:
For each test case in a new line print 1 if the string 'a' can be obtained by rotating string 'b' by two places else print 0.

Constraints:
1<=T<=50
1<=length of a, b <100

Example:
Input:
2
amazon
azonam
geeksforgeeks
geeksgeeksfor
Output:
1
0
"""


def is_rotated(first_string, second_string):
    if first_string == second_string[2:] + second_string[:2] or first_string == second_string[-2:] + second_string[:-2]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        first_string = input()
        second_string = input()
        print(is_rotated(first_string, second_string))