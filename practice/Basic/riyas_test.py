"""
Riya loves to play with strings. She discoverd her own kind of strings which passed the Riya's Test. When split from the middle, the string gives two halves having the same characters and same frequency of each character. If the number of characters in the string are odd,  ignore the middle character and check for the 2 halves to pass the Riya's Test. For example, papa passes the Riya's Test, since the two halves pa and pa have the same characters with the same frequency.
eefefe and bananb pass Riya's Test. Note that motor, abcd, color, flipflop fails Riya's Test. Given a string, find out whether the string passes Riya's Test or not.


Input: the First line of input contains a single integer T, i.e number of test cases.Each test case contains a string A  " containing lowercase English alphabet".


Output:  For each test case, Print "YES" if string Pass in Riya test else  "NO".


Constraints:

1 ≤ T ≤ 100
2 ≤ Length of string A ≤ 1000

Example:
Input:
6
lala
color
motor
pqrpqr
abbaab
abdbc


Output:
YES
NO
NO
YES
NO
NO



Explanation :
  Test Case 1: string  lala passes Riya's Test, as the strings gives two halves having the same characters and same frequency of each character.
"""


def riyas_test(str):
    l = len(str)
    if l % 2 == 0:
        first, second = str[:int(l / 2)], str[int(l / 2):]
    else:
        first, second = str[:int(l / 2)], str[int(l / 2) + 1:]
    if sorted(first) == sorted(second):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(riyas_test(str))
