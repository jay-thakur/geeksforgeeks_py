"""
You have given a non-empty string. This string consists of lowercase or uppercase or both English letters. The length of the string will not exceed 1000.

Convert the string using following cases:

Case 1: If first character of string is in lowercase then second character should be in uppercase, third character should be in lowercase and so on till the last character of the string.

   For example :   Input   geeksforgeeks

                            Output   gEeKsFoRgEeKs

Case 2: If first character of string is in uppercase then second character should be in lowercase, third character should be in uppercase and so on till the last character of the string.

  For example :   Input    Geeksforgeeks

                           Output   GeEkSfOrGeEkS

Input

       •   The first line of the input contains a single integer T denoting the number of test cases.

The first line of each test case contains a string.
Output

For each test case, output the require string in newline.


Constraints

    •    1 ≤ T ≤ 100


Example

Input:
2
geeksforgeeks
Geeksforgeeks

Output:
gEeKsFoRgEeKs
GeEkSfOrGeEkS
"""


def crazy_string(str):
    str2 = ''
    c = 1
    if str[0].islower():
        c = 0
    for ele in str:
        if c == 0:
            str2 += ele.lower()
            c += 1
        else:
            str2 += ele.upper()
            c -= 1
    return str2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(crazy_string(str))
