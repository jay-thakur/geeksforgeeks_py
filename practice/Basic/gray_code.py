"""
Given a decimal number n. Find the gray code of this number in decimal form.

Input:
The first line contains an integer T, the number of test cases. For each test case, there is an integer n denoting the number

Output:
For each test case, the output is gray code equivalent of n.

Constraints:
1<=T<=100
0<=n<=10^8

Example:
Input
2
7
10
Output
4
15

Explanation:
1.7 is represented as 111 in binary form. The gray code of 111 is 100, in the binary form whose decimal equivalent is 4.
2. 10 is represented as 1010 in binary form. The gray code of 1010 is 1111, in the binary form whose decimal equivalent is 15.
"""


def gray_code(n):
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n)[2:]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        p = (bin(n)[2:])
        q = gray_code(p)        
        print(int(q, 2))