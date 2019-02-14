"""
A thief trying to escape from a jail has to cross N walls each with varying heights. He climbs X feet every time. But, due to the slippery nature of those walls, every times he slips back by Y feet.  Now the task is to calculate the total number of jumps required to cross all walls and escape from the jail.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two space separated integers X, Y, N. Then in the next line are N space separated values denoting the heights ( Ht[] ) of the walls.

Output:
For each test case in a new line print the total number of jumps.

Constraints:
1<=T<=100
1<= N, X, Y <=100
1<= Ht[] <=1000

Example:
Input:
2
10 1 1
5
4 1 5
6 9 11 4 5

Output:
1
12
"""
import math


def thief_trying_to_escape(arr, x, y):
    sum = 0
    for h in arr:
        if x >= h:
            a = 1
        else:
            a = math.ceil((h - y) / (x - y))
        sum = sum + a
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        x, y, n = [int(i) for i in input().split()][0:3]
        arr = [int(i) for i in input().split()][0:n]
        print(thief_trying_to_escape(arr, x, y))
