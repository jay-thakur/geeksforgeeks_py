"""
Check if  a given number is perfect or not. A number is perfect if  sum of factorial of its digit is equal to the given number. For example 145 is a Perfect Number because 1! + 4! + 5! = 145

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The next T lines will contain an integer N.

Output:
Corresponding to each test case, in a new line, print "Perfect " if it follow above condition else print "Not Perfect"  without quotes.

Constraints:

1 ≤ T ≤ 50

1 ≤ N ≤ 10000


Example:

Input:

2

23

145

Output:
Not Perfect
Perfect
"""


import math


def perfect_number(n):
    sum = 0
    while n > 0:
        rem = n % 10;
        n = n // 10;
        sum = sum + math.factorial(rem)

    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        temp = n
        sum = perfect_number(n)
        if sum == temp:
            print("Perfect");
        else:
            print("Not Perfect")