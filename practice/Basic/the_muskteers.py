"""
Aditi and Nandi are very good friends and never want to go far from each other. Their friendship is defined in a string of '0' and '1' . Help them to check that they are far from each other or not. There is only one way to check, all 0's should be together, it means they are not far from each other.

Input:
First line consists of the test case T. The only line of each test case consists of string , consisting of 0 and 1.

Output:
If they are not far from each other print "YES" else "NO".

Constraints:
1<=T<=100
1<=|Length of string|<=10000

Example:
Input:
3
000
111
0001110
Output:
YES
NO
NO
"""


def the_muskteers(s):
    c = s.replace('1', " ")
    d = list(map(str, c.split()))
    if len(d) > 1 or len(d) == 0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(the_muskteers(s))
