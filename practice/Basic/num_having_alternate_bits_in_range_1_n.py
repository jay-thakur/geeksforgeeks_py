"""
Given a positive integer n. The problem is to print the numbers in the range 1 to n having bits in alternate pattern. Here alternate pattern means that the set and unset bits in the number occur in alternate order. For example- 5 has an alternate pattern i.e. 101.

INPUT: The first line consists of an integer T i.e. the number of test cases. Each test case has the single line input, denoting the integer n.

OUTPUT: Print all the numbers with alternate bits in the range 1 to n.

CONSTRAINTS:
1<=T<=100
1<=n<=105

EXAMPLES:
INPUT :
2
10
50

OUTPUT : 
1 2 5 10
1 2 5 10 21 42
"""


def num_having_alternate_bit(n):
    initial = 1
    while n > initial:
        print(initial, end=' ')
        if initial % 2 == 1:
            initial *= 2
        else:
            initial *= 2
            initial += 1
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        num_having_alternate_bit(n)
