"""
For a given string of binary number find the two’s complement of it.

Input :
The first line contains an integer 'T' denoting the total number of test cases.The next T lines contains the string S.

Output:
â€¨In each separate line the two’s complement string should be output.

Constraints:
1<=T<=30
1<=length(string)<=10

Example:
Input:
1
00000101

Output:
11111011
"""


def twos_complement(num, n):
    for i in range(n - 1, -1, -1):
        if num[i] == '1':
            for j in range(i - 1, -1, -1):
                if num[j] == '1':
                    num[j] = '0'
                else:
                    num[j] = '1'
            break
    return ''.join(num)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num = list(input())
        print(twos_complement(num, len(num)))
