"""
Given a number as integer s, find the sum of all the elements present in all possible subsequences of s.

Input:
The first line of the input contains an integer T denoting the number of test cases. For each test case, there is a integer s as input.

Output:
For each test case, the output is an integer displaying the sum of all possible subsequences of s.

Constraints:
1<=T<=100
1<=S<=10^6

Example:
Input:
1
123
Output:
24

Explanation:
All possible sub-sequences are 1, 2, 3, {1, 2}, {2, 3}, {1, 3}, {1, 2, 3} which add up to 24.
"""


def sum_of_all_subsequences_of_a_num(arr):
    ans = 0
    n = len(arr)
    for i in range(0, n):
        ans = ans + int(arr[i])

    return ans * pow(2, n - 1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input()
        print(sum_of_all_subsequences_of_a_num(arr))
