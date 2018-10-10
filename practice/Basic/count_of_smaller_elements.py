"""
Given an sorted array of size n. Find number of elements which are less than or equal to given element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then the next line contains n space separated integers forming the array.

Output:
Print the number of elements which are less than or equal to given element.

Constraints:
1<=T<=10^5
1<=n<=10^5
1<=a[i]<=10^5

Example:
Input:
2
6
1 2 4 5 8 10
9
7
1 2 2 2 5 7 9
2

Output:
5
4
"""


def count_of_smaller_elements(arr, n):
    count = 0
    for j in arr:
        if int(j) <= n:
            count = count + 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        n = int(input())
        print(count_of_smaller_elements(arr, n))
