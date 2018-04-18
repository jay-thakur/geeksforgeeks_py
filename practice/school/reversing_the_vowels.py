"""
Given a string, reverse only the vowels present in it and print the resulting string.


Input: First line of the input file contains an integer T denoting the number of test cases. Then T test cases follow. Each test case has a single line containing a string.

Output: Corresponding to each test case, output the string with vowels reversed.

Example:

Input:
4
geeksforgeeks
practice
wannacry
ransomware

Output:
geeksforgeeks
prectica
wannacry
rensamwora
"""


def reversing_the_vowels(str):
    vowels = []
    for i in str:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(i)
    vowels = vowels[::-1]

    j = 0

    for i in range(len(str)):
        if str[i] in ['a', 'e', 'i', 'o', 'u']:
            str = str[0:i] + vowels[j] + str[i + 1:]
            j += 1
    return str


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(reversing_the_vowels(str))
