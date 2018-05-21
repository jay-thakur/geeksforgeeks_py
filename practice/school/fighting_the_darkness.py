"""
Given an integer array representing size of candles which reduce 1 unit in a day. Room is illuminated using given x candles. Question is to find maximum number of days room is without darkness.

Input:
The first line of input consists of an integer T denoting the number of test cases Each test case contains an integer N denoting the size of the array. Then in the next line are N space separated elements of the array.

Output:
For each test case print the maximum number of days room will be illuminated in a new line.
Constraints:
1<=T<=200
1<=N<=1000
1<=Elements of array <=10^7

Example:
Input:
1
5
2 3 4 1 2
Output:
4
"""


def fighting_the_darkness(arr):
    return max(arr)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(fighting_the_darkness(arr))
