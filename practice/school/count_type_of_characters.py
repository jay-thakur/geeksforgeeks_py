"""
Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a string S.
Output:
For each test case, print four lines. In the first line print the count of upper case letters, in the second line print the count of lower case letters, in the third line print the count of numbers and in the fourth line print the count of special characters present in the string S.

Note: The strings doesnot contains whitespaces.

Constraints:
1<=T<=100
1<=length(S)<=100000

Example:
Input:
2
#GeeKs01fOr@gEEks07
*GeEkS4GeEkS*
Output:
5
8
4
2
6
4
1
2
"""


def count_type_of_characters(str):
    lower_case, upper_case, special_char, num_char = 0, 0, 0, 0
    for i in str:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
        elif i.isnumeric():
            num_char += 1
        else:
            special_char += 1
    print(upper_case)
    print(lower_case)
    print(num_char)
    print(special_char)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        count_type_of_characters(str)
