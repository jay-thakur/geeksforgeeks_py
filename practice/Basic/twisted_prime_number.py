"""
A number is said to be twisted prime if it is a prime number and reverse of the number is also a prime number.

Input:
The first line of input contains an integer T denoting the number of test cases. The first and last line of each test case consists of an integer n.

Output:
Print the answer in "Yes" or "No".

Constraints:
1<=T<=100
2<=n<=100000

Example:
Input:
2
97
43

Output:
Yes
No
"""
import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def twisted_prime_number(n):
    k = n[::-1]
    if is_prime(int(n)) and is_prime(int(k)):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(twisted_prime_number(n))
