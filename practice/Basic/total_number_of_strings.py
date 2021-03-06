"""
Given 3 characters a, b, c. Find the number of strings of length n that can be formed from these 3 characters. Given that : we can use ‘a’ as many times as we want, ‘b’ maximum once, and ‘c’ maximum twice.

Input:
The first line of input contains an integer T denoting the number of test cases. The first and last line of each test case consists of an integer n.

Output:
Print the total number of string that can be formed.

Constraints:
1<=T<=20
1<=N<=20

Example:
Input:
2
3
5

Output:
19
71
"""


def total_number_of_strings(n):
    return 1 + n * 2 + (n ** 3 - n) // 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(total_number_of_strings(n))
