"""
Given an array arr[ ] of size n such that elements of arr[ ] in range [0, 1, ..n-1]. Our task is to divide the array into the maximum number of partitions that can be sorted individually, then concatenated to make the whole array sorted.

Input:
The first line of the input contains an integer T, the number of test cases. For each test case, the first line contains an integer n, denoting the size of the array arr. Next line contains n- space separated integers denoting the elements of the array arr.

Output:
For each test case, the output is an integer displaying the maximum number of partitions.

Constraints:
1<=T<=100
1<=n<=25

Example:
Input:
2
4
2 1 0 3
6
2 1 0 3 4 5
Output:
2
4

Explanation:
1. If divide arr[] into two partitions {2, 1, 0} and {3}, sort then and concatenate then, we get the whole array sorted.
2. The maximum number of partitions are four, we get these partitions as {2, 1, 0}, {3}, {4} and {5}
"""


def maxi_no_of_partitions(arr):
    count = 0
    max_element = 0
    for i, e in enumerate(arr):
        max_element = max(max_element, e)
        if i == max_element:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(maxi_no_of_partitions(arr))
