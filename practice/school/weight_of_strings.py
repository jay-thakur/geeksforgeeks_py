"""
You are given two strings S1 and S2. You need to find weights of both strings and compare them. The weight of a string can be obtained by adding individual weights of the characters that make the string. The weight of individual characters are the position on which they occur in the english alphabets table; for eg, a has weight 1, z has weight 26.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines
The first string S1
The second string S2

Output:
Print 1 if the weight of the first string is greater. Print 2 if the weight of the second string is greater. Print equal if the the weights are equal.

Constraints:
1<=T<=100
1<=|S1|<=1000
1<=|S2|<=1000

Example:

Input:
4
batman
superman
kira
l
goku
broly
manbat
batman

Output:
2
1
2
equal

Note: The strings contains only lowercase characters.
"""


def weight_of_strings(str1, str2):
    res1 = 0
    res2 = 0

    for i in str1:
        res1 += (ord(i) - 96)
    for i in str2:
        res2 += (ord(i) - 96)

    if res1 > res2:
        return 1
    elif res2 > res1:
        return 2
    else:
        return "equal"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        print(weight_of_strings(str1, str2))
