"""
Given a sorted array and a value x, find the number of array elements less than or equal to x and elements more than or equal to x.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and X,N is the size of array.
The second line of each test case contains N input C[i].

Output:

Print the number of Array elements less than or equal to x and Array elements greater than or equal to x.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 100
0 ≤ X ≤ 1000
1 ≤ C[i] ≤ 200

Example:

Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
0 7
2 5
4 4
"""


def smaller_and_larger(arr, n, x):
    smaller_count = larger_count = 0
    for val in arr:
        if val <= x:
            smaller_count += 1
        if val >= x:
            larger_count += 1
    return smaller_count, larger_count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = map(int, input().split())
        arr = [int(x) for x in input().split()]
        smaller_count, larger_count = smaller_and_larger(arr, n, x)
        print(smaller_count, larger_count)
