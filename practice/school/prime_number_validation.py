"""
Check the given number is prime or not using JAVA regex.

Input:
First line consists of T test cases. Only line of every test case consists of an integer N.

Output:
Print "1" if the given number statement is prime else 0.

Constraints:
1<=T<=100
1<=N<=1000

Example:
Input:
2
3
4

Output:
1
0
"""


def prime_number_validation(n):
    count = 0
    for i in range(2, n // 2 + 1):
        if (n % i) == 0:
            count = 1
            break
    if count == 1:
        return "0"
    else:
        return "1"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(prime_number_validation(n))
