"""
Given a number, the task is to set all odd bits of a number.

INPUT: The first line consists of an integer T i.e. the number of test cases. Each test case contains an integer n .

OUTPUT: For each test case, print the number formed after setting all the odd bits of the given number in newline.

CONSTRAINTS:

1<=T<=100
1<=n<=105

EXAMPLES:
INPUT :
2
20
10

OUTPUT :
21
15

EXPLANATION:

Input : 20
Output : 21
Explanation : Binary representation of 20
is 10100. Setting all odd
bits make the number 10101 which is binary
representation of 21.

Input : 10
Output : 15
"""


def set_all_odd_bits(n):
    temp = n
    i = 0
    while temp > 0:
        if i % 2 == 0:
            n = n | (1 << i)
        i += 1
        temp >>= 1
    return n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(set_all_odd_bits(n))
