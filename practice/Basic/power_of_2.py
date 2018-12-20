"""
Given a positive integer N, check if N is a power of 2.

Input:
The first line contains 'T' denoting the number of test cases. Then follows description of test cases.
Each test case contains a single positive integer N.


Output:
Print "YES" if it is a power of 2 else "NO". (Without the double quotes)


Constraints:
1<=T<=100
0<=N<=10^18

Example:
Input :
2
1
98

Output :
YES
​NO

Explanation:  (2^0 == 1)
"""


def is_power_of_2(n):
    if n == 0:
        return 0
    else:
        return n & (n - 1) == 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if is_power_of_2(n):
            print("YES")
        else:
            print("NO")
