"""
Given n in Gray code equivalent. Find its binary equivalent.

Input:
The first line contains an integer T, number of test cases. For each test cases, there is an integer n denoting the number in gray equivalent.

Output:
For each test case, the output is the decimal equivalent number n of binary form.

Constraints:
1<=T<=100
0<=n<=10^8

Example:
Input
2
4
15
Output
7
10

Explanation:
1. 4 is represented as 100 and its binary equivalent is 111 whose decimal equivalent is 7.
2. 15 is represented as 1111 and its binary equivalent is 1010 i.e. 10 in decimal.
"""


def gray_to_binary_equivalent(n):
    n = str(bin(n)[2:])
    res = [n[0]]
    for i in range(1, len(n)):
        res.append(int(n[i]) + int(res[i - 1]))
        if res[i] == 2:
            res[i] = 0
    ans = ''.join(str(i) for i in res)
    return int(ans, 2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(gray_to_binary_equivalent(n))
