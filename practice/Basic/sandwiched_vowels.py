"""
For a given string S, comprising of only lowercase English alphabets, eliminate the vowels from the string that occur between two consonants(sandwiched between two immediately adjacent consonants). Print the updated string on a new line.

Input:

First line of input is an integer T, denoting the number of test cases. For each test case, input the string S on a new line.

Output:

For each test case, the only line of output is the updated string after omission of all sandwiched vowels.

Constraints:

1<=T<=100

3<=L<=10, where L is length of string S

'a'<=S[i]<='z', i is an integer denoting index of S


Example:

Input:

5
bab
ceghij
aaii
gghho
saaafor

Output:

bb
cghj
aaii
gghho
saaafr

Explanation:

In the first test case, a is a vowel occuring between two consonants i.e. b. Hence the updated string eliminates a.
In the second test case, e and i are the vowels occurring between tow consonants. Hence they are removed from the string.
In the third and fourth test cases, there is no such vowel that occurs between two consonants. Hence the string remains unchanged.
In the fifth test case, o occurs between f and r which are consonants, hence is eliminated.
"""


def sandwiched_vowels(s):
    strr = s[0]
    for j in range(1, len(s) - 1):
        if s[j] in "aeiou":
            if not (s[j - 1] not in "aeiou" and s[j + 1] not in "aeiou"):
                strr += s[j]
        else:
            strr += s[j]
    return strr + s[len(s) - 1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(sandwiched_vowels(s))
