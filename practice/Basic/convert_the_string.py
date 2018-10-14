"""
Given a string S(consisting of uppercase/lowercase alphabets only), change the string s according to the rules provided below:

Delete all the vowels from the string.
Insert # in front of all the consonants.
Change the case of all the letters of the string.
​NOTE: If the required string is null print "-1".

INPUT: The first line consists of an integer T i.e. the number of test cases. First and the last line of each test case consists of an string S.

OUTPUT: Print the required string after conversion.

CONSTRAINTS:

1<=T<=100
1<=|Length of string|<=105

EXAMPLES:
INPUT :
2
aBAcAba
SunshinE

OUTPUT :
#b#C#B
#s#N#S#H#N
"""


def convert_the_string(str):
    ans = ""
    for char in str:
        if char.lower() not in ('a', 'e', 'i', 'o', 'u'):
            ans += "#" + char
    return ans.swapcase()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(convert_the_string(str))
