"""
Remove all characters from an alphanumeric string.

Input:
The first line of the input contains T denoting the number of testcases. First line of each test case will be an alphanumeric string.

Output:
 For each test case output will be a numeric string after removing all the characters.

Constraints:
1 <= T <= 30
1 <= size of string <= 100

Example:

Input:
1
AA123BB4

Output:
1234
"""
def remove_char(string):
    for ch in string:
        if ch.isdigit():
            print(ch, end='')
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        string = input()
        remove_char(string)