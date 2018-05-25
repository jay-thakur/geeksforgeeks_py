"""
A ZERO number is a number which has zeroes present in it, but there should be no zero present in the beginning of the number. For example 3210, 8050896, 70709 are all ZERO numbers whereas 02364, 03401 are not.
The task is to check whether the given number is a ZERO number or not.

Examples:
Input : 707069
Output : It is a ZERO number.
Explanation: 707069 does not contains zeros at the beginning.

Input : 02364
Output : It is not a ZERO number.
Explanation: in 02364 there is a zero at the beginning of the number.
Input :
The first line of input contains an integer T denoting the Test cases. Then T test cases follow.
Second line contains value of N.

Output :
Yes, if N is ZERO Number; else NO

Constraints :
1 ≤ T ≤ 150
1 ≤ N ≤ 100000

Input :
3
0
10001
11111

Output :
NO
YES
NO
"""


def zero_number(str):
    if str[0] == '0':
        result = 'NO'
    elif '0' in str[1:]:
        result = 'YES'
    else:
        result = 'NO'
    return result


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(zero_number(str))
