"""
Given a string, find the minimum number of changes to it so that all substrings of the string become distinct.

Input:
The first line contains an integer T, number of test cases. For each test case, there is a string s.

Output:
For each test case, the output is an integer displaying the minimum number of changes in the string.

Constraints:
1<=T<=100
1<=s.length()<=26

Example:
Input
3
aab
aebaecedabbee
ab
Output
1
8
0

Explanation
1.If we change one instance of 'a' to any character from 'c' to 'z', we get all distinct substrings.
2. We need to change 2 a's, 2 b's and 4 e's to get distinct substrings.
3. As no change is required hence 0.
"""


def mini_changes_to_make_all_substrings_distinct(str):
    return len(str) - len(set(str))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(mini_changes_to_make_all_substrings_distinct(str))
