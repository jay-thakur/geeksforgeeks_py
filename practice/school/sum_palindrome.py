"""
Given a number, reverse it and add it to itself unless it becomes a palindrome or the the count becomes 5 times. If it becomes a palindrome then print that palindrome number, otherwise print -1.

Input: First line of the input contains an integer T denoting the number of test cases. Each test case has a single line containing a number.

Output: Corresponding to each test case, print the palindrome number or -1 as stated above.

Constraints:
1 <= T <= 200
1 <= N <=1000

Example:
Input:
2
23
30
Output:
55
33
"""


def sum_palindrome(n):
    count = 0
    while count <= 5:
        if n == n[::-1]:
            return n
            break
        else:
            value = int(n) + int(n[::-1])
            n = str(value)
            count += 1
    return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(sum_palindrome(n))
