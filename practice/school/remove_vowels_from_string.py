"""
Given a string, remove the vowels from the string and print the string without vowels.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists of a string s.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=|Length of string|<=1000

Example:
Input:
2
welcome to geeksforgeeks
what is your name ?

Output:
wlcm t gksfrgks
wht s yr nm ?
"""


def remove_vowels_from_strings(s):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return ''.join([c for c in s if c not in vowels])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(remove_vowels_from_strings(s))
