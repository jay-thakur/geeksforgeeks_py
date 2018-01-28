"""
Starting from one print a series of asterisk(*) till N terms with increasing order and difference being 1.

Input:
First line of the input is the number of test cases T. And first line of test case contain the value of 'N'.

Output:
Series of asterisk's is printed in a single line with one space between each iteration.

Constraints:
1 <=T<= 30
1 <=N<= 100

Example:

Input:


5
1
10
5
6
2

Output:
 

*
* ** *** **** ***** ****** ******* ******** ********* **********
* ** *** **** *****
* ** *** **** ***** ******
* **
"""


def print_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*',end='')
        print(end=' ')
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print_pattern(n)