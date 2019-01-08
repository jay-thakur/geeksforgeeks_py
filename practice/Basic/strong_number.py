"""
Write a program to check whether a number is strong or not. A number is called strong number if sum of the factorial of its digit is equal to number itself. For example: 145 as 1! + 4! + 5! = 1 + 24 + 120 = 145

Input:

First line contains number of test cases T. Then following T lines contains an integer N.


Output:

Output "Strong" if given number is strong else "Not Strong" .

Constraints:

1<=T<=50
0<=N<=1000


Example:

Input:
2
145
10

Output:
Strong
Not Strong
"""
import math


def strong_number(n):
    total = 0
    for i in n:
        total += math.factorial(int(i))

    if total == int(n):
        return "Strong"
    else:
        return "Not Strong"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(strong_number(n))
