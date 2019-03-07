"""
Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string containing alphanumeric characters.

Output:
Print the sum of all numbers present in the string.

Constraints:
1<=T<=10^5
1<=length of the string<=10^5

Example:
Input:
4
1abc23
geeks4geeks
1abc2x30yz67
123abc

Output:
24
4
100
123
"""
import re


def sum_of_numbers_in_string(s):
    n = re.findall('\d+', s)
    return sum(int(k) for k in n)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(sum_of_numbers_in_string(s))
