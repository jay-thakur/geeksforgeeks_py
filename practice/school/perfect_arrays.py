"""
Given an N length array and you have to tell whether the array is perfect or not.An array is said to be perfect if it's reverse array matches the original array. If the array is perfect then print "PERFECT" else print "NOT PERFECT".

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an integer N (size of the array)and the second line contains N elements a1,a2,......aN of an array .

Output:
For each test case, print either "PERFECT" or "NOT PERFECT" in new line as your answer.

Constraints:
1<=T<=100
1<=N<=100

1<=aN<=1000

Example:
Input:
2
5
1 2 3 2 1
5
1 2 3 4 5
Output:
PERFECT
NOT PERFECT
"""


def perfect_arrays(arr):
    if arr == arr[::-1]:
        return "PERFECT"
    else:
        return "NOT PERFECT"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(perfect_arrays(arr))
