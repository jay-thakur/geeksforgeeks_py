"""
Given a string, we have to find the longest word in the input string and then calculate the number of characters in this word.

Input:
The first line of input contains an integer T,  number of test cases. For each test case, there is a string s.

Output:
For each test case, the output is an integer denoting the length of the longest word in the sentence.

Constraints:
1<=T<=100

Example:

Input:
2
A computer science portal for geeks
I am an intern at geeksforgeeks

Output
8
13
"""


def longest_word(str):
    max = 0
    for word in str:
        if len(word) > max:
            max = len(word)
    return max


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input().split()
        print(longest_word(str))
