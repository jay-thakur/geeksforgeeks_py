"""
Given a number N, the task is to find the sum of all the elements from all possible subsets of a set formed by first N natural numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a number N as input.

Output:
For each test case, print the sum in new line.

Constraints:
1 <= T <= 50
1 <= N <= 50

Example:
Input:
2
2
3

Output:
6
24

Explanation:

Input :  n = 2
Output : 6
Possible subsets are {{1}, {2},
{1, 2}}. Sum of elements in subsets
is 1 + 2 + 1 + 2 = 6.
"""


def sum_of_all_subsets(n):
    ans = (((n * (n + 1)) // 2) * (pow(2, (n - 1))))
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_all_subsets(n))