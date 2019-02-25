"""
A surpasser of an element of an array is a greater element to its right, therefore x[j] is a surpasser of x[i] if i < j and x[i] < x[j]. The surpasser count of an element is the number of surpassers.
Given an array of distinct integers, for each element of the array find its surpasser count i.e. count the number of elements to the right that are greater than that element.


Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.


Output:

Corresponding to each test case, in a new line, print the surpasser count i.e. count the number of elements to the right that are greater than that element.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:

Input
1
5
4 5 1 2 3

Output
1 0 2 1 0
"""


def surpasser_count(arr, size):
    res = []
    for i in range(size):
        count = 0
        for j in range(i + 1, size):
            if arr[i] < arr[j]:
                count += 1
        res.append(count)
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*surpasser_count(arr, size))
