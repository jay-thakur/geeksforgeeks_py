"""
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Input:
The first line contains 'T' denoting the number of testcases. Then follows description of testcases.
Each case begins with a single positive integer N denoting the size of array.
The second line contains the N space separated positive integers denoting the elements of array A.

Output:
For each testcase, print "Yes" or  "No" whtether it is Pythagorean Triplet or not (without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= A[i] <= 1000

Example:
Input:
1
5
3 2 4 6 5
Output:
Yes

Explanation:
For testcase1: a=3, b=4, and c=5 forms a pythagorean triplet, so we print "Yes"
"""


def pythagorean_triplet(arr, size):
    d = {}
    for x in arr:
        d[x * x] = 1

    for i in range(size - 1):
        for j in range(i + 1, size):
            if (arr[i] * arr[i] + arr[j] * arr[j]) in d:
                return 'Yes'
    return 'No'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(pythagorean_triplet(arr, size))
