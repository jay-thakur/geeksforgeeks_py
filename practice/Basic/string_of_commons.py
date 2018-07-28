"""
Given two strings, S and R, composed of only English alphabets (both upper and lower cases), find the alphabets that occur in both the strings. Print the common alphabets (if any) as output in ascending order of their ASCII values.

Input:

First line of input is an integer T, denoting the number of test cases. For each test case, first line of input is the string S and second line is the string R. Repetition is allowed in both the strings.

Output:


The only line of output for each test case is the list of alphabets that occur in both S and R. Upper and lower case alphabets are treated to be distinct from each other i.e. 'A' and 'a' will be regarded two different letters. The letters are printed on a new line in ascending order of ASCII values i.e. capital letters in common will be printed first in the output. If there are no common letters in S and R, print "nil" as output (without quotes).

Constraints:

1<=T<=100
1<=|S|,|R|<=100, denoting length of strings.

Example:

Input:

3
tUvGH
Hhev
aabb
ccII
xYzab
YYoxb

Output:

Hv
nil
Ybx

Explanation:

The letters common in the first test case are H and v. Hence output is, Hv.

In the second test case, there is nothing common. Hence output is nil.

In the third test case, Y,b,x are common. Hence output is, Ybx.
"""


def string_of_commons(s, r):
    s = sorted(s)
    r = sorted(r)
    ans = sorted(list(set(s).intersection(r)))
    if not ans:
        print('nil')
    else:
        print(''.join(ans))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        r = input()
        string_of_commons(s, r)
