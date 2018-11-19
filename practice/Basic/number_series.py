"""
Ishaan's friend, Charul, gave a challenge to Ishaan. He gave a series to Ishaan and asked him to find the Nth term of that series.
Ishaan is very weak at solving series, so he needs your help. Help him find the Nth term of the following series :
N    Nth term
1    0
2    1
3    0
4    2
.
.
.
10    1

Input :
First line of input contains a single integer T denoting the number of test cases.
The only line of each test case contains an integer N.

Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 200
1 <= N <= 10^9

Example :
Input :
5
1
2
3
4
10
Output :
0
1
0
2
1

Explanation :
The Nth term is given, solve the series.
"""


def number_series(n):
    count = 0
    while int(n / 2) - n / 2 == 0:
        n = n / 2
        count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(number_series(n))
