"""
You are given an array A[] , you have to construct a new array A2[].
The values in A2[] are obtained by doing OR of consecutive elements in array.

Input:
First line of the input contains t, the number of test cases. Each line of the test case contains a number n specifying the number of elements.
Each 'n' lines denoting elements of array A[].

Output:
Each new line of the output contains element of array A2[] .

Constraints:
1<=T<=100
1<=n<=100000
1<=A[i]<=100000



Example:

Sample Input 0
1
5
10 11 1 2 3

Sample Output 0
11 11 3 3 3
"""


def play_with_or(arr, size):
    for i in range(size - 1):
        arr[i] = arr[i] | arr[i + 1]
    return arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*play_with_or(arr, size))
