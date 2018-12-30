"""
For a given string delete the elements which are appearing more than once consecutively. All letters are of lowercase.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases,  a string will be inserted.


Output:
In each seperate line the modified string should be output.


Constraints:
1<=T<=31
1<=length(string)<=100


Example:
Input:
1
aababbccd

Output:
ababcd
"""


def consecutive_elements(s):
    result = ''
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            continue
        else:
            result += s[i]
    result += s[i + 1]
    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(consecutive_elements(s))
