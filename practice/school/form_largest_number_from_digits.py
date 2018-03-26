"""
Given an array of digits form 0 to 9 of size n, the task is to rearrange elements of the array such that after combining all the elements of the array number formed is maximum.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains an integer n denoting the number of elements in the array. Then in the next line are n space seperated integers denoting the elements of the array.

Output:
For each test case print a single line a number denoting the largest number that can be achieved by rearranging the elements of the array.

Constraints:
1<=T<=100
1<=n<=18

Example:
Input:
2
5
9 0 1 3 0
3
1 2 3

Output:
93100
321
"""


def largest_number_from_digits(arr):
    arr.sort(reverse=True)
    return arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        arr = largest_number_from_digits(arr)
        for e in arr:
            print(e, end='')
        print()