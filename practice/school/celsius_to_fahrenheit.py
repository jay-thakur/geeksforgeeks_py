"""
Given a temperature in celsius, convert and print in farenheit.

Note: We need to print the floor value of the result.

Input:
The first line of input contains T denoting number of testcases. Each testcase contains single integer denoting the temperature in celsius.

Output:
For each testcase, output the temperature in farenheit.

Constraints:
1<=T<=100
1<=temperature in celsius<=100

Example:

Input:
1
32

Output:
89
"""


def convert_celsius_to_fahrenheit(c):
    return int((c * 9/5) + 32)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        c = float(input())
        print(convert_celsius_to_fahrenheit(c))