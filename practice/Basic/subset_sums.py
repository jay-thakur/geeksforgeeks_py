"""


Given an array of integers, print sums of all subsets in it. Output should be printed in increasing order of sums.

Input : arr[] = {2, 3}
Output: 0 2 3 5

Input : arr[] = {2, 4, 5}
Output : 0 2 4 5 6 7 9 11

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case is N, N is the size of array. The second line of each test case contains N space separated values of the array arr[].

Output:

Output for each test case should be space separated sums in increasing order.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 10
0 ≤ A[i] ≤ 100

Input:
2
2
1 2
3
5 2 1

Output:

0 1 2 3
0 1 2 3 5 6 7 8

"""


def subset_sums(arr, size):
    li = []
    size = 2 ** size
    for i in range(size):
        su = 0
        for j in range(size):
            if i & (1 << j):
                su += arr[j]
        li.append(su)
    return sorted(li)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*subset_sums(arr, size))
