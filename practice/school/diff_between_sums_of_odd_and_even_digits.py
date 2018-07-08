"""
Given a long integer, we need to find if the difference between sum of digits present at the odd positions and sum of digits present at even positions is 0 or not. The indexes start from zero (0 index is for leftmost digit).

Input:
First line consists of T test cases. Only line of every test case consists of a number N.

Output:
Print "Yes" if difference is 0 else print "No".

Constraints:
1<=T<=300
1<=N<=10^18

Example:
Input:
2
1212112
123
Output:
Yes
No
"""


def diff_between_sums_of_odd_and_even_digits(n):
    even_sum = 0
    odd_sum = 0
    for i in range(len(n)):
        if i % 2 == 0:
            even_sum += int(n[i])
        else:
            odd_sum += int(n[i])
    if even_sum - odd_sum == 0:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input().strip()
        print(diff_between_sums_of_odd_and_even_digits(n))
