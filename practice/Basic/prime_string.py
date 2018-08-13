"""
Provided a String of length N, your task is to find out whether or not the given string is a prime string. A prime string is a string in which the sum of the ASCII value of all the characters is prime.

Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test case follows. The first line of each test case contains an integer N denoting the length of the string, next line contains the input string str of length N.

Output:
For each test case print "YES" if the string is prime string else print "NO", on a new line.


Constraints:
1<=T<=102
1<=N<=108

Example:
Input
3
13
geeksforgeeks
4
JiiT
5
India

Output

YES
NO
NO
"""


def is_prime(n):
    rng = int(n ** 0.5)
    for i in range(2, rng + 1):
        if n % i == 0:
            return "NO"
    return "YES"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        str = input()[0:n]

        ascii = sum(ord(c) for c in str)
        print(is_prime(ascii))
