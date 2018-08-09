"""
Given a string s, remove all consonants and prints the string s that contains vowels only.
Input: The first line of input contains integer T denoting the number of test cases. For each test case, we input a string.
Output: For each test case, we get a string containing only vowels. If the string doesn't contain any vowels, then print "No Vowel"

Constraints:

1<=T<=100

The string should consist of only alphabets.

Examples:

Input: geEks
Output: eE
Input: what are you doing
Output: a ae ou oi
"""


def remove_consonants_from_a_string(str):
    x = ''
    for i in str:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']:
            x += i
    if len(x) > 0:
        return x
    else:
        return 'No Vowel'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(remove_consonants_from_a_string(str))
