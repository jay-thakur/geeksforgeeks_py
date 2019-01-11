"""
Write a program to check whether a number is wierd or not. A weird number is weird if the sum of the proper divisors (divisors including 1 but not itself) of the number is greater than the number, but no subset of those divisors sums to the number itself.

Example:

The smallest weird number is 70. Its proper divisors are 1, 2, 5, 7, 10, 14, and 35; these sum to 74, but no subset of these sums to 70. The number 12, for example, is not weird, because the proper divisors of 12 are 1, 2, 3, 4, and 6, sum of divisors is 16; but there is a subset {2, 4, 6} with sum 12, i.e., 2+4+6 = 12.

Input:

First line contains number of test cases T. Then following T lines contains an integer N.


Output:

Output "Weird" if given number is strong else "Not Weird" .

Constraints:

1<=T<=100
2<=N<=10000


Example:

Input:
2
5
70

Output:
Not Weird
Weird
"""


def weird_number(n):
    weirds = [70, 836, 4030, 5830, 7192, 7912, 9272]
    if n in weirds:
        return "Weird"
    else:
        return "Not Weird"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(weird_number(n))
