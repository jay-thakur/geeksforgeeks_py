"""
Given an integer represented as a string, we need to get the sum of all possible sub-strings of this string.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains a string S that represents a number..

Output:
For each test case, in a new line, print the required result.

Constraints:
1 <= T <= 100
1 <= S <= 1012

Example:
Input:
2
1234
421
Output:
1670
491

Explanation:
Testcase1:
Input  : N = “1234”
Output : 1670
Sum = 1 + 2 + 3 + 4 + 12 + 23 +
       34 + 123 + 234 + 1234
    = 1670
Testcase2:
Input  : N = “421”
Output : 491
Sum = 4 + 2 + 1 + 42 + 21 + 421
    = 491
"""


def sum_of_all_substrings_a_num(s):
    n = len(s)
    sum = 0
    for i in range(n):
        for j in range(n, i, -1):
            sum += int(s[i:j])
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(sum_of_all_substrings_a_num(s))
