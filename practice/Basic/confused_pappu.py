"""
Pappu is confused between 6 & 9 . He works in billing department of abc company and his work is to return the remaining amount to the customers. If actual remaining amount is given we need to find the maximum possible extra amount given by the pappu to the customers.

For ex:- actual remaining amount = 56

so, maximum possible extra amount =  (59 - 56 ) = 3

Input

    The first line of the input contains a single integer T denoting the number of test cases.
    The first line of each test case contains N (actual remaining amount).

Output

For each test case, output the maximum possible extra amount in newline.

Constraints

    •    1 ≤ T ≤ 102

    •    1 ≤ N≤ 10000001

Example

Input:

3
6
66
666

Output:

3
33
333
"""


def confused_pappu(n):
    n = str(n)
    x = n.replace('6', '9')
    return int(x) - int(n)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(confused_pappu(n))
