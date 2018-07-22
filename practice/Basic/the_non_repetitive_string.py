"""
Shreyansh has been given a string for evaluation by his teacher. He needs to find out whether the given string is non-repetitive or not.
A non-repetitive string is defined as a string which does not contain any different character between 2 same characters (Refer example for explanation).

Input :
The first line of input contains a single integer T denoting the number of test cases. Each test case contains a string S which consists only of upper-case English alphabets.

Output :
For each test case, print 1 if the string is non-repetitive, else print 0 in a new line.

Constraints :
1 <= T <= 200
2 <= Length of String S <= 10^4

Example :
Input :
3
AAABCDD
AABBAA
ABCDA

Output :
1
0
0

Explanation : 
Case 1 :
AAABCDD
Here no different character is placed between 2 same characters.

Case 2 :
AABBAA
Here 2 B's are placed between 2 A's, so this is not a non-repetitive string.

Case 3 :
ABCDA
Here 1 B, 1 C, 1 D are placed between 2 A's, so this is not a non-repetitive string.
"""


def the_non_repetitive_string(str):
    vis = [0] * 26
    vis[ord(str[0]) - ord('A')] = 1

    ans = 1
    for i in range(1, len(str)):
        if str[i] != str[i - 1] and vis[ord(str[i]) - ord('A')] == 1:
            ans = 0
            break
        vis[ord(str[i]) - ord('A')] = 1
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(the_non_repetitive_string(str))
