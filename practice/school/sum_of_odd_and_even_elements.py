"""
Given an integer N, you have to print the sum of odd numbers and even numbers form 1 to N

Input:
First line consists of T test cases. First line of every test case consists of a Single integer N.

Output:
Single line output, with sum of odd numbers and even numbers respectively.

Constraints:
1<=T<=100
1<=N<=10^5

Example:
Input:
2
5
6
Output:
9 6
9 12
"""


def sum_of_odd_and_even_elements(n):
    odd, even = 1, 2
    for i in range(3, n + 1):
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return odd, even


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(*sum_of_odd_and_even_elements(n))
