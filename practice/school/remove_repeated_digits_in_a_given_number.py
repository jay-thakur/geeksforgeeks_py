"""
Given an integer N, remove consecutive repeated digits from it.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the integer N.

Output:

Print the number after removing consecutive digits. Print the answer for each test case in a new line.


Constraints:

1<= T <=100

1<= N <=1018


Example:

Input:

1
12224

Output:
124
"""


def remove_repeated_digits(n):
    result = n[0]
    for j in range(1, len(n)):
        if n[j - 1] != n[j]:
            result += n[j]
    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(remove_repeated_digits(n))
