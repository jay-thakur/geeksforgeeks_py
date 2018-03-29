"""
Babul likes to play with string and he always tries do something new with it. This time he found a very typical way to sort a string. What he did is that he took a string composed of both lowercase and uppercase letters and sorted it in such a manner such that the uppercase and lowercase letter comes in an alternate manner but in sorted way, but Babul has to do some other stuffs also, so he needs your help to complete this job as fast as possible.

Example:

Input: bAwutndekWEdkd

Output: AbEdWddekkntuw

Explanation:
Here we can see that letter ‘A’,’E’,’W’ are sorted as well as letters “b,d,d,d,e,k,k,n,t,u,w” are sorted but both appears alternately in the string as far as possible.


Input:
The first line of input contains an integer T denoting the no of test cases.Then T test cases follow. Each line of test case will contain a string S.


Output:
For each test case in a new line print the required output.


Constraints:
1<=T<=100
1<=|S|<=1000


Example:
Input:
2
bAwutndekWEdkd
AFBRi

Output:
AbEdWddekkntuw
AiBFR
"""


def unusual_string_sort(str):
    lower = []
    upper = []
    for i in str:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)

    upper = sorted(upper)
    lower = sorted(lower)

    for i in range(min(len(lower), len(upper))):
        print(upper[i] + lower[i], end='')
    if len(lower) > len(upper):
        lower = lower[i + 1:len(lower)]
        print(''.join(lower))
    else:
        upper = upper[i + 1:len(upper)]
        print(''.join(upper))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        unusual_string_sort(str)