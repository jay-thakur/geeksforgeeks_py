"""
Given an array A of non-zero, positive integers, sort the array in ascending order such that element at the Kth position in unsorted array stays unmoved and all other elements are sorted. Other sorted elements are placed in positions other than the Kth position i.e. before and after it. Print the resultant array.

Input:

First line of input is an integer T, denoting the number of test cases. For each test case, first line takes two integers. First, the integer N, denoting size of the array and second the integer K  denoting the position of the element that has to be kept unmoved. The second line of test case consists of N-space separated non-zero, positive integers representing elements of A. Repetition of elements is allowed.

Output:

The only line of output for each test case is the resultant array after the strange sort.

Constraints:

1<=T<=100
2<=N<=100
1<=K<=N
1<=A[i]<=100, where i is the index of the array

Example:

Input:

3
5 2
3 12 30 79 2
10 5
16 16 18 10 9 22 11 5 35 22
8 3
9 2 5 2 1 10 12 4

Output:

2 12 3 30 79
5 10 11 16 9 16 18 22 22 35
1 2 5 2 4 9 10 12

Explanation:

In the first test case, element at position 2 needs to be kept unmoved. On sorting the remaining elements we get, 2 3 30 79. Therefore, 12 is given position 2 in the sorted array which gives result as 2 12 3 30 79.

In the second test case, 5th position in unsorted array is 9. All other elements are sorted and 9 is given the 5th position again in the sorted array.

In the third test case, 3rd element 5, is kept unmoved. After sorting operation and inserting 5 again as 3rd element we get the required output.
"""


def strange_sort(arr):
    arr[k - 1], arr[-1] = arr[-1], arr[k - 1]
    new_arr = sorted(arr[:-1])
    new_arr.insert(k - 1, arr[-1])
    return new_arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n]
        print(*strange_sort(arr))
