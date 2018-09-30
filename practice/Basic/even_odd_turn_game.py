"""
Given three positive integers X, Y and P. Here P denotes the number of turns. Whenever the turn is odd X is multiplied by 2 and in every even turn Y is multiplied by 2. The task is to find the value of max(X, Y) ÷ min(X, Y) after the complete P turns.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing three integers X,Y and P.

Output:

For each test case, print the value of max(X, Y) ÷ min(X, Y) after the complete P turns .
Constraints:

1<=T<=100

1<=X<=Y<=P<=1000
Example:

Input:
2
1 2 1
3 7 2

Output:
1
2
"""


def even_odd_turn_game(x, y, p):
    for j in range(1, p + 1):
        if j % 2 == 0:
            y *= 2
        else:
            x *= 2
    return int(max(x, y) / min(x, y))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        x, y, p = [int(i) for i in input().split()][0:3]
        print(even_odd_turn_game(x, y, p))
