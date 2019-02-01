"""
Given an array of n words. Some words are repeated twice, we need count such words.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the number of words in the string. The next line contains n space separated words forming the string.

Output:
Print the count of the words which are repeated twice in the string.

Constraints:
1<=T<=105
1<=no of words<=105
1<=length of each word<=105

Example:
Input:
2
10
hate love peace love peace hate love peace love peace
8
Tom Jerry Thomas Tom Jerry Courage Tom Courage

Output:
1
2
"""


def twice_counter(arr):
    c = 0
    for i in arr:
        if arr.count(i) == 2:
            c += 1
            arr.remove(i)
    return c


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [i for i in input().split()][0:size]
        print(twice_counter(arr))
