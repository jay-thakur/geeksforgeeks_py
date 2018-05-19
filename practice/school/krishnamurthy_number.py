"""
A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself. Given a number N as input. Write a program to check whether this number is krishnamurthy number or not.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a single integer N.

Output:
For each test case print "YES" without quotes if N is a Krishnamurthy Number otherwise print "NO".

Constraints:
1<=T<=100
1<=N<=105

Example:
Input:
2
145
235
Output:
YES
NO
"""


def k_num(n):
    sum = 0
    for i in n:
        if i != "0":
            fact = 1
            for j in range(1, int(i) + 1):
                fact *= j
            sum += fact
    if int(n) == sum:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(k_num(n))
