"""
Write a program to print all sophie germain number less than n. A prime number p is called a sophie prime number if 2p+1 is also a prime number. The number 2p+1 is called a safe prime. For example 11 is a prime number and 11*2 + 1 = 23 is also a prime number so, 11 is sophie germain prime number .

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.

Output:
For each testcase, print  all sophie germain number less than n.

Constraints:

1<=T<=100
3<=10000<=N

Example:
Input:
1
25

Output:
2 3 5 11 23

Explanation:  For p =2 ,  2p+1 = 5 which is also a prime. Similarly for 3 = 7, for 5 = 11, for 11 = 23, for 23 = 47 all are primes. So for every mentioned primes, 2p+1 is also prime which satisfies sophie germain prime number condition.

"""
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print('2', end=' ')
        for i in range(3, n, +2):
            if is_prime(i) and is_prime(2 * i + 1):
                print(i, end=' ')
        print()
