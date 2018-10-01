"""
You are given a string that contains, in addition to words, a phone number. The phone number is of the format +dd-ddddddddddd.
Here d represents a digit. Your task is to extract the phone number from the string and print it.

Input:
The first line of input contains an integer T denoting the number of test

cases. T test cases follow. Each test case contains a single line of string.

Output:
Print the phone number.

Constraints:
1<=T<=100

Example:

Input:
2
Call me +91-90549385612
The number is +24-01087860699

Output:
+91-90549385612
+24-01087860699

Note: See that the leading zero in +24-01087860699 is also included. Also, every string contains exactly one phone number.
"""


def extract_the_phone_num(s):
    for j in s:
        if j[0] == '+' and j[3] == '-' and len(j) == 15:
            print(j)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = [i for i in input().split()]
        extract_the_phone_num(s)
