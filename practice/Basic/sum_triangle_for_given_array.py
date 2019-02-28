"""
Given a array, write a program to construct a triangle where last row contains elements of given array, every element of second last row contains sum of below two elements and so on.

Example:
Input: arr[] = {4, 7, 3, 6, 7};
Output:
81
40 41
21 19 22
11 10 9 13
4 7 3 6 7

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then next line contains n space separated integers forming the array.

Output:
Output the sum triangle for the input array with space separated integers.

Constraints:
1<=T<=1000
1<=N<=1000
1<=Ai<=1000

Example:
Input:
2
5
4 7 3 6 7
7
5 8 1 2 4 3 14

Output:
81 40 41 21 19 22 11 10 9 13 4 7 3 6 7
200 98 102 55 43 59 34 21 22 37 22 12 9 13 24 13 9 3 6 7 17 5 8 1 2 4 3 14
"""


def sum_triangle_for_given_array(arr, size):
    while size:
        temp = []
        for i in range(size - 1):
            temp.append(arr[i] + arr[i + 1])
        for i in temp[::-1]:
            arr.insert(0, i)
        size = size - 1
    return arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(sum_triangle_for_given_array(arr, size))
