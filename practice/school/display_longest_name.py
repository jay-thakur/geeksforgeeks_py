"""
Given a list of names, display the longest name.

Input: First line of input contains an integer T, the number of test cases. T test cases follows. First line of each test case contains an integer N, i.e total number of names. Next N lines contains names of different length.


Output: Longest name in the list of names.


Constraints:

1<=T<=10
1<=N<=10


Example:

Input:
1
5
Geek
Geeks
Geeksfor
GeeksforGeek
GeeksforGeeks

Output:
GeeksforGeeks
"""


def longest_name(arr):
    return max(arr, key=len)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = []
        for j in range(1, n + 1):
            arr.append(input())
        print(longest_name(arr))
