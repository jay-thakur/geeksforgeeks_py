"""
Given a non-negative integer N. The problem is to check if binary representation of n is palindrome or not. Note that the actual binary representation of the number is being considered for palindrome checking, no leading 0’s are being considered.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test case contains a single line of input denoting the number N.

Output:
For each test case, print 1 if binary representation of N is palindrome; else print 0.

Constraints:
1<=T<=200
0<=N<=263-1

Example:

Input:
3
1
2
3

Output:
1
0
1

Explanation:
For testcase 2: The binary representation of 2 is 10, and of course, 10 is not a palindrome.
For testcase 3: The binary representation of 3 is 11, needless to say, 11 is a palindrome.
"""


def if_binary_rep_of_a_num_is_palindrome(n):
    b = bin(n)
    b = b[2:]
    if b == b[::-1]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(if_binary_rep_of_a_num_is_palindrome(n))
