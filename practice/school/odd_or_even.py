"""

Given a positive integer determine whether it is odd or even.

Input:
First line contains an integer, the number of test cases 'T' Each test case should contain a positive integer N.


Output:
In each seperate line print "odd" if odd and "even" if even.(Dont print the quotes)


Constraints:
1<=T<=30
0<=N<=50


Example:
Input:
1
23

Output:
odd

"""


def odd_or_even(n):
    if n % 2 == 0:
        return 'even'
    return 'odd'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(odd_or_even(n))