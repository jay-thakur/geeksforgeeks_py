"""
Given an array containing N words, you need to find the most frequent word in the array. If multiple words have same frequency then print the word that comes first in lexicographical order.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test case contains 2 lines:-
The size of array N
N words separated by spaces

Output:
For each testcase, print the most frequent word.

Constraints:
1<=T<=100
1<=N<=1000

Example:

Input:
3
3
geeks for geeks
2
hello world
3
world wide fund

Output:
geeks
hello
fund

Explanation:
For testcase 1: geeks comes 2 times.
For testcase 2: hello and world both have 1 frequency. We print hello as it comes first in lexicographical order.
"""


def most_freq_word_in_array(str_arr):
    str_arr.sort()
    s2 = []
    for i in str_arr:
        s2.append(str_arr.count(i))
    return str_arr[s2.index(max(s2))]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        str_arr = [i for i in input().split()][0:n]
        print(most_freq_word_in_array(str_arr))
