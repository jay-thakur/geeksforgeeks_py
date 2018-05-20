"""
Given a number N. You need to write a program to count the number of digits in N which evenly divides N.

Input:
First line of input contains an integer T which denotes the number of test cases. T test cases follows. First line of each test case contains a single integer N.

Output:
For each test case in a new line print the total number of digits of N which evenly divides N.

Constraints:
1<=T<=200
1<=N<=105

Example:
Input:
3
12
1012
23
Output:
2
3
0
"""


def count_digits(n):
    count = 0
    for i in str(n):
        if i != "0" and n % int(i) == 0:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_digits(n))
