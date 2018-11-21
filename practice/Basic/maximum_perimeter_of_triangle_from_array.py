"""
Given an Array of non-negative integers. Find out the maximum perimeter of the triangle from the array.

Input:
The first line contains an integer T, the number of test cases. For each test case, the first line contains an integer n, the size of the array. Next line contains n- space separated integers.

Output:
For each test case, the output is an integer displaying the maximum perimeter if the triangle is possible else print -1.

Constraints:
1<=T<=100
3<=n<=100

Example:
Input
2
6
6 1 6 5 8 4
7
7 55 20 1 4 33 12
Output
20
-1

Explanation:
1. Triangle formed by  8,6 & 6. Thus perimeter 20.
2. As the triangle is not possible because the condition: the sum of two sides should be greater than third is not fulfilled here.
"""


def maximum_perimeter_of_triangle(arr):
    n = sorted(arr)
    size = len(n) - 1
    for i in range(len(n) - 2):
        if n[size - i] < n[size - i - 1] + n[size - i - 2]:
            return n[size - i] + n[size - i - 1] + n[size - i - 2]

    return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(maximum_perimeter_of_triangle(arr))
