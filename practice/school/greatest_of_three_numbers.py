"""
Write a program to find the greatest of the three numbers.

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain three positive numbers a,b and c.

Output:
Print maximum of three numbers.

Constraints:
1<=T<=30
1<=a<=1000
1<=b<=1000
1<=c<=1000

Example:
Input:
1
10 3 2

Output:
10
"""


def greatest_of_three_numbers(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c :
        return b
    elif c > a and c > b:
        return c


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        numbers = list([int(i) for i in input().split()][0:3])
        a, b, c = numbers[0], numbers[1], numbers[2]
        print(greatest_of_three_numbers(a, b, c))