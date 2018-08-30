"""
Input N number of arrays and print the merged array in ascending order containing only unique elements.
Input:
The first line consists of T test cases and then next line consists of number of arrays denoted by N and then next of each N lines contain a number n denoting the number of elements in an array.
Output:
Output in one line the merged array sorted in ascending order.
Constraints:
1<=T<=50
1<=N<=4
1<=Ai<=100
Example:
Input:
1
3
3
1 2 8
2
4 9
3
1 2 8
Output:
1 2 4 8 9
"""


def merge_and_sort(arr):
    return sorted(list(set(arr)))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        no_of_arrays = int(input())
        arr = []
        for i in range(no_of_arrays):
            size = int(input())
            arr += [int(i) for i in input().split()][0:size]
        print(*merge_and_sort(arr))
