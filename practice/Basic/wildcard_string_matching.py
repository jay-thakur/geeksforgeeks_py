"""
Given two strings where first string may contain wild card characters and second string is a normal string. Write a function that returns true if the two strings match. The following are allowed wild card characters in first string.

* --> Matches with 0 or more instances of any character
      or set of characters.
? --> Matches with any one character.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two strings, a string with wildcard and one without.

Output:
Print "Yes" (without quotes) if the two strings match else print "No" (without quotes).

Constraints:
1<=T<=10^5
1<=length of the two string<=10^5

Example:
Input:
2
ge*ks
geeks
ge?ks*
geeksforgeeks

Output:
Yes
Yes
"""
from fnmatch import fnmatch


def wind_string_matching(s1, s2):
    fil = fnmatch(s2, s1)
    if fil:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        print(wind_string_matching(s1, s2))
