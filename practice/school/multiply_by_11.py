"""
Today Kevin’s Teacher taught Kevin, Multiplication table of 11.After reaching home, Kevin thought of multiplying the numbers with 11 and
finding the answers.Help Kevin finding the answers as soon as possible.

Input: First line of input contains T number i.e number of test cases, each test case followed by T numbers.

output: For each test case, Print a single integer.

Constraints:
0<=T<=100
0< Number of Digits in Integer <=1000000

Input:
3
8
12
15

Output:
88
132
165
Explaination:

Test case1  :  8*11 = 88
Test case2 : 12*11 = 132
Test case3 : 15*11 = 165
"""


def multiply_by_11(n):
    return n * 11


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(multiply_by_11(n))
