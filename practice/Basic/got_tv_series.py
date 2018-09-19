"""
Ishaan has finally started watching a new TV series, Game of Thrones. He watches a certain number of episodes every day. Given a day N, find out how many episodes does Ishaan watch on the Nth day.
He watches the following number of episodes on the given days :
N    Number of Episodes
1    1
2    2
3    6
4    4
.
.
.
10    20

Input :
The first line of input contains a single integer T denoting the number of test cases.each test case contains an integer N.

Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 200
1 <= N <= 10^12

Example :
Input :
5
1
2
3
4
10
Output :
1
2
6
4
20
"""


def got_tv_series(n):
    return ("{0:b}".format(n).count("1"))*n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(got_tv_series(n))
