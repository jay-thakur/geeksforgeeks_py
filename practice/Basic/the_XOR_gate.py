"""
Construct an N input XOR Gate. An XOR Gate returns 1 if odd number of its inputs are 1, otherwise 0.

Input:
The first line of input takes the number of test cases, T. Then T test cases follow.Each test case consists of 2 lines. The first line of each test case takes the number of inputs to the XOR Gate, N. The second line of each test case takes N space separated integers denoting the inputs to the  XOR Gate. Note that the inputs can be either 1's or 0's.


Output:
For each test case on a new line print the output of the N input XOR Gate.

Constraints:

1<=T<=100
1<=N<=100

Example:

Input:

3
2
1 1
3
1 0 1
4
1 1 1 0

Output:
0
0
1
"""


def the_XOR_gate(arr):
    if sum(arr) % 2 == 0:
        return 0
    return 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(the_XOR_gate(arr))
