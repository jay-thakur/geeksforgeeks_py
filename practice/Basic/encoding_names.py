"""
CBI agents are investigating a case in which they came across certain names of the culprits.They decided to encode the names into the number format.

"Riya" is encoded as "729611390","Sumitha" as "73108101981109993" ,"Anandita" as "55101891039410011294" and so on...Help them to encode the names.

Input:

First line of input contains an integer T denoting the number of test cases.T lines follow each of which containes a string S denoting the name of the culprits.
Output:

For each test case,print the encoded Integer in a new line.
Constraints:

1<=T<=100 and Names contains only english alphabets
Example:

Input
3
Soni
Mona
Pawan

Output
7310210298
6710210290
708811190104
"""


def encoding_names(s):
    ans = ""
    for i in range(len(s)):
        ans += str(ord(s[i]) - 10 + i)
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(encoding_names(s))
