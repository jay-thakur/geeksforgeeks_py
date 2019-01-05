"""
Given a random set of numbers, Print them in sorted order.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print each sorted array in a seperate line. For each array its numbers should be seperated by space.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 1000
1 ≤A[i]<100

Example:
Input:
1
2
3 1

Output:
1 3
"""


def sort_the_array(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return ' '.join(str(x) for x in arr)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(sort_the_array(arr, size))
