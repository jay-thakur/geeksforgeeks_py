"""
Given an input stream of N integers (alongwith the operation on these integers), the task is to print the number of the distinct elements in the stream after each operation.
There can be two types of operations that can be performed:

Addition represented by A.
Deletion represented by R.
Input:
First line of the input contains an integer T denoting the number of test cases. Then T test case follows. First line of each test case contains an integer N denoting the number of operations to be performed on a stream. Next N lines two space separated elements, the operation to be performed and the key element.

Output:
For each operation output the number of the distinct characters in a stream on a new line.

Constraints:
1<=N<=106
1<=A[]<=106

Example:
Input:
1
8
A 5
A 5
A 7
R 5
R 7
A 1
A 2
R 2
Output:
1
1
2
2
1
2
3
2
"""


def distinct_elements_in_a_stream():
    d = dict()
    for i in range(n):
        op, num = input().split(" ")
        if op == "A":
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        else:
            if num in d:
                if d[num] > 1:
                    d[num] -= 1
                else:
                    d.pop(num)
        print(len(d))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        distinct_elements_in_a_stream()
