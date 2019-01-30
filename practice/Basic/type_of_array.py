"""
You are given an array of size N having no duplicate elements. The array can be categorized into following:
1.  Ascending
2.  Descending
3.  Descending Rotated
4.  Ascending Rotated
Your task is to print which type of array it is and the maximum element of that array.

Input:
The first line of input contains an integer T denoting the no test cases. Then T test caes follow. Each testcase contains two lines of input. The first line contains an integer N denoting the size of the array. The next line contains N space separated values of the array.

Output:
For each test case, print the largest element in the array and and integer x denoting the type of the array.

Constraints:
1 <= T <= 100
3 <= N <= 107
1 <= A[] <= 1018

Example:
Input:
2
5
2 1 5 4 3
5
3 4 5 1 2

Output:
5 3
5 4

Explanation:
Testcase1:
Input : A[] = { 2, 1, 5, 4, 3}
Output : Descending rotated with maximum element 5
Testcase2:
Input : A[] = { 3, 4, 5, 1, 2}
Output : Ascending rotated with maximum element 5
"""


def type_of_array(arr):
    b = max(arr)
    c = min(arr)
    if arr.index(b) == 0 and arr.index(c) == len(arr) - 1:
        return [b, "2"]
    elif arr.index(c) == 0 and arr.index(b) == len(arr) - 1:
        return b, "1"
    elif arr.index(b) == arr.index(c) + 1:
        return b, "3"
    else:
        return b, "4"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*type_of_array(arr))
