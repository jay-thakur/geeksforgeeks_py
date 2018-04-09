"""
You will be given two numbers A and B. Your task is to print 1 if A < B, print 2 if A > B and print 3 if A = B.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case contains an integer A and the second line of each test case contains an integer B. There might be leading zeros.


Output:

Corresponding to each test case, in a new line, print 1, 2 or 3 accordingly if A < B, A > B or A = B.


Constraints:

1 ≤ T ≤ 100

0 ≤ A, B ≤ 10155


Example:

Input

3
1234
12345
100
1
00999
100

Output

1
2
2
"""


def compare(a, b):
    if a < b:
        return 1
    elif a > b:
        return 2
    else:
        return 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        print(compare(a, b))
