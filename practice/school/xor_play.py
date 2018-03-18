"""
Given an integer, you have to tell all the proper divisors (all divisors except the no. itself) of the number N in sorted manner. You also have to perform XOR operation on all these divisors and print the corresponding result.

Input :
The first line of input contains an integer T denoting the Test cases. Then T test cases follow. Each test case contains an integer N.

Output :
For each test case print 2 lines. In the first line print space separated values denoting the proper divisors of N. Then in the next line print the XOR of all the proper divisors of N.

Constraints :
1 ≤ T ≤ 110
1 ≤ N ≤ 1012

Example:
Input :
2
10
8

Output :
1 2 5
6
1 2 4
7

Explanation :
Test case 1 : 1 XOR 2 XOR 5 = 6
Test case 2 : 1 XOR 2 XOR 4 = 7
"""
import math


def find_divisors(n):
    print(1, end=' ')
    divisors = []
    xor = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print(i, end=' ')
            if i != (n // i):
                divisors.append(str(n // i))
                xor = xor ^ i ^ n // i
            else:
                xor = xor ^ i

    print(" ".join(divisors[::-1]))
    print(xor)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        find_divisors(n)