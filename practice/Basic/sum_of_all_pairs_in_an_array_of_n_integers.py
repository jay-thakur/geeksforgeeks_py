"""
Given an array A of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j) such that (1 <= i < j <= n).
f(a[i], a[j]):       If | a[j]-a[i] | > 1

                         f(a[i], a[j]) = a[j] - a[i]

                         Else  if | a[j]-a[i] | <= 1

                         f(a[i], a[j]) = 0

Input:
The first line of the input contains T denoting the number of test cases. For each test case, the first line contains integer n denoting the size of the array A, followed by n space separated integers denoting the element of array A.

Output:
For each test case, the output is an integer denoting the sumof f(a[i],a[j]) of all pairs.

Constraints:
1<=T<=100
1<=n<=50

Example:
Input:
2
4
6 6 4 4
5
1 2 3 1 3
Output:
-8
4

Explanation:
1. All pairs are: (6 - 6) + (4 - 6) + (4 - 6) + (4 - 6) + (4 - 6) + (4 - 4) = -8
2. The pairs that add up are: (3, 1), (3, 1) to give 4, rest all pairs according to condition gives 0.
"""


def sum_of_all_pairs_in_an_array_of_n_integers(arr, size):
    res = 0
    for i in range(size):
        for j in range(i + 1, size):
            if abs(arr[j] - arr[i]) > 1:
                res += arr[j] - arr[i]
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(sum_of_all_pairs_in_an_array_of_n_integers(arr, size))