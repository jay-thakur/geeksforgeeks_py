"""
You are given an array of size N. You need to find elements which appear prime number of times in the array with minimum K frequency (frequency >= K).

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains two lines of input:-
The size of the array N and minimum frequency K separated by a space.
The elements of the array separated by spaces.

Output:
For each testcase, print the elements that have prime frequency with their frequency >=K. Print the output in sorted order. If there are no such elements then print -1.

Constraints:
1<=T<=105
1<=N<=1000
1<=K<=10
1<=A[i]<=10000

Example:

Input:
2
13 2
11 11 11 23 11 37 51 37 37 51 51 51 51
3 1
11 22 33

Output:
37 51
-1

Explanation:
For testcase 1: 11's count is 4, 23 count 1, 37 count 3, 51 count 5. 37 and 51 are two number that appear prime number of time and frequencies greater than or equal to K=2.
For testcase 2: K=1, and all three elements occur extactly 1 times. Unfortunately, 1 is not prime, so we don't print any element. We, instead, print a -1.
"""


import math


def prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def num_with_prime_freq_greater_than_or_equal_to_k(times, data):
    c = []
    data.sort()

    for i in data:
        if prime(data.count(i)):
            if data.count(i) >= times:
                if i not in c:
                    c.append(i)
    if len(c) != 0:
        return c
    else:
        return [-1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, times = [int(i) for i in input().split()][0:2]
        data = [int(i) for i in input().split()][0:n]
        res = num_with_prime_freq_greater_than_or_equal_to_k(times, data)
        for i in res:
            print(i, end=" ")
        print()
