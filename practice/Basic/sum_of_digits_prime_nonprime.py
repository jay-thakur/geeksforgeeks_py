"""
Given a number N, you need to write a program that finds the sum of digits of the number till the number becomes a single digit and then check whether the number is Prime/Non-Prime.
Example:

Input : 5602
Output: No
Step 1- 5+6+0+2 = 13
Step 2- 1+3 = 4
4 is not prime

Input : 56
Output : Yes
Step 1- 5+6 = 11
Step 2- 1+1 = 2 hence 2 is prime
Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. The only lone of each testcase contains the integer N.

Output:
For each test case print "P" if the resultant is prime and "NP" if the number is Non-prime.

Constraints:
1<=T<=103
1<=N<=105

Example:
Input:
2
1903
25
Output:
NP
P
"""


def isprime(n):
    if len(str(n)) > 1:
        st = 0
        for i in range(len(str(n))):
            st = st + int(str(n)[i])
        return isprime(st)
    else:
        return n


def sum_of_digits_prime_nonprime(n):
    a = isprime(n)
    if a == 2 or a == 3 or a == 5 or a == 7:
        return "P"
    else:
        return "NP"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_digits_prime_nonprime(n))
