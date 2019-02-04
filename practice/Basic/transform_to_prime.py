"""
Given an array of n integers. Find minimum number to be inserted in array, so that sum of all elements of array becomes prime. If sum is already prime, then return 0.

Input:
First line consists of T test cases. The T testcases follow. First line of every test case consists of N, denoting number of elements of array. Second line of every test case consists of elements of array.

Output:
Single line output, print the required answer.

Constraints:
1<=T<=100
1<=N<=1000

Example:
Input:
1
5
2 4 6 8 12
Output:
5
"""


def checkPrime(num):
    for i in range(2, int((num / 2) + 1)):
        if num % i == 0:
            return 1
    return 0


def transform_to_prime(arr):
    num = sum(arr)
    a = checkPrime(num)
    count = 0
    while a != 0:
        num = num + 1
        count = count + 1
        a = checkPrime(num)
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(transform_to_prime(arr))
