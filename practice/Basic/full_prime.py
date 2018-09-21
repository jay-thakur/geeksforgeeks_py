"""
Given a number n, check if it is Full Prime or not.
Note : A full prime number is one in which the number itself is prime and all its digits are also prime.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

Output:
Print 'Yes' if it is full prime,otherwise print 'No'.

Constraints:
1<=T<=100
1<=N<=100000

Example:

Input:
2
53
41

Output:
Yes
No
"""
from math import sqrt


def isprime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def full_prime(n):
    prime = ['2', '3', '5', '7']
    if isprime(n):
        ans = "Yes"
        for num in str(n):
            if num not in prime:
                ans = "No"
                break
        return ans
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(full_prime(n))
