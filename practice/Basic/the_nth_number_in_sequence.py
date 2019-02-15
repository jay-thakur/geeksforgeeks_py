"""
Consider the sequence of numbers 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, ... In this sequence first we have the number 1, then the numbers from 1 to 2, then the numbers from 1 to 3 and so on. Your task is to find the Nth number in this sequence.


Input :
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a positive integer which denotes N.


Output :
For each test case in a new line print the Nth number in the given sequence.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1010

Example :
Input :
3
4
14
114

Output :
1
4
9
"""


def nth_number_in_sequence(n):
    d = (1 + 4 * 2 * n)
    root = int((-1 + d ** .5) / 2)
    if int((root * (root + 1)) / 2) == n:
        return root
    else:
        return n - int((root * (root + 1)) / 2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(nth_number_in_sequence(n))
