"""
Given three distinct numbers, find the number with value in middle (Try to do it with minimum comparisons).

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain three distinct numbers a, b and c.


Output:
Print middle of three numbers.


Constraints:
1<=T<=30
-1000<=a, b, c<=1000

Example:
Input:
2
20 30 40
12 32 11

Output:
30
12
"""


def middle_of_three(arr):
    arr.sort()
    return arr[1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = [int(i) for i in input().split()][0:3]
        print(middle_of_three(arr))