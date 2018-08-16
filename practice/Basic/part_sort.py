"""
Given an array A[N], you are required to sort the array in given index range [a, b], i.e., you need to sort subarray A[a..b]
Input :
The first line of input contains an integer T denoting the Test cases. Then T test cases follow.
The first line contains an integer N i.e number of array elements.
The second line contains array elements A[i]
The third line contains a and b

Output :
For each test case, the output is the sorted array as per the given range [a, b]

Constraints :
1 ≤ T ≤ 100
1 ≤ N ≤ 10^5
0 ≤ A[i] ≤ 10^6
0 ≤ a<=b ≤ N-1

Input :
1
5
7 8 4 5 2
1 4

Output : 
7 2 4 5 8
"""


def part_sort(arr, a, b):
    a, b = min(a, b), max(a, b)
    sort_arr = sorted(arr[a:b + 1])
    return arr[:a] + sort_arr + arr[b + 1:]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()][0:n]
        a, b = [int(i) for i in input().split()][0:2]
        print(*part_sort(arr, a, b))
