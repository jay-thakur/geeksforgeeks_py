"""
Construct an N input OR Gate. An OR Gate returns 0 if all its inputs are 0, otherwise 1.

Input:

The first line of input takes the number of test cases, T. Then T test cases follow.

Each test case consists of 2 lines.

The first line of each test case takes the number of inputs to the OR Gate, N. The second line of each test case takes N space separated integers denoting the inputs to the OR Gate. Note that the inputs can be either 1's or 0's.

Output:

Print the output of the N input OR Gate for each test case on a new line.

Constraints:

1<=T<=100

1<=N<=100

Example:

Input:

3
2
1 1
3
0 0 0
4
1 1 1 0

Output:

1
0
1
"""


def the_OR_gate(arr):
    for i in arr:
        if i == 1:
            return 1
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(the_OR_gate(arr))
