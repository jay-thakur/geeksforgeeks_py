"""
Given an array A of positive integers, sort the array in ascending order such that element at index K in unsorted array stays unmoved and all other elements are sorted.

Input:
The first line contains an integer T, number of test cases. For each test case, there is an integer n denoting the size of the array A. Next line contains n space separated integers denoting the elements of the array. Next line contains an integer k denoting the index.

Output:
For each test case, the output is the sorted array except the element at index k.

Constraints:
1<=T<=100
1<=n<=50

Example:
Input
2
6
10 4 11 7 6 20
2
3
30 20 10
0
Output
4 6 11 7 10 20
30 10 20
"""


def sorting_all_arr_elements_except_one(arr, k):
    num = arr[k]
    sor_arr = sorted(arr[:k] + arr[k + 1:])
    sor_arr.insert(k, num)
    return sor_arr


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        k = int(input())
        print(*sorting_all_arr_elements_except_one(arr, k))
