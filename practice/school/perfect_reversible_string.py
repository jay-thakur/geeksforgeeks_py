"""
You are given a string ‘str’, the task is to check that reverses of all possible substrings of ‘str’ are present in ‘str’?

Input : str = "ab"
Output: 0
// all substrings are "a","b","ab" but reverse
// of "ab" is not present in str

Input : str = "aba"
Output: 1

Input:
The first line contains 'T' denoting the number of testcases. Then follows description of testcases.
Each case begins with a single integer N denoting the length of string. The next line contains the string s.


Output:
Print "1" if it is a palindrome else "1". (Without the double quotes)


Constraints:
1<=T<=30
1<=N<=100


Example:
Input:
2
3
aba
5
abcde

Output:
1
0
"""


def perfect_reversible_string(word):
    if word == word[::-1]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        word = input()
        print(perfect_reversible_string(word))
