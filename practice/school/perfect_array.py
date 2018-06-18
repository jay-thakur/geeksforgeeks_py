"""
There is an array contains some non-negative integers. Check whether the array is perfect or not. An array is called perfect if it is first strictly increasing, then constant and finally strictly decreasing. Any of the three parts can be empty.

Input:
The first line of the input contains an integer T, denoting number of test cases. The first line of each test case contains an integer N denoting the size of the array. The second line of each test cases N space separated integers.
Output:
For each test case, print "Yes" if it satisfies the condition else "No".

Constraints:
1<=T<=100
1<=N<=10^3
Each element in the array will be in range [1,100000]

Example:
Input:
2
6
1 8 8 8 3 2
5
1 1 2 2 1
Output:
Yes
No
"""


def perfect_array(arr, size):
    j = 0
    while j < size - 1 and arr[j] < arr[j + 1]: j += 1
    while j < size - 1 and arr[j] == arr[j + 1]: j += 1
    while j < size - 1 and arr[j] > arr[j + 1]: j += 1
    if j == size - 1:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(perfect_array(arr, size))
