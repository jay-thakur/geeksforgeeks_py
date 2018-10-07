"""
It’s time to find out which player is consistent in cricket. You need to calculate the average of a
player based on his score. Player average is defined as total runs scored by a player in N matches
divided by the number of matches in which he gets out. If the answer is too large you need to print
“-1” (without inverted comma’s).

Input:

The first line of the input contains T denoting number of test cases.

First line of each test case contains N denoting number of matches.

Next N line contains an integer denoting the number of runs scored by player in that match followed by a string which can be "out" or "notout" depending on whetherthe player is out or not-out in the match.

Output:

You need to print average of the player. If answer is not an integer take ceil and print your answer.


Constraints:
1<=T<=10
1<=N<=400
0<=Runs scored in a single match<=300

Example:
Input:
1
5
40 out
20 notout
13 out
60 notout
100 out
Output:
78
"""


from math import ceil


def cricket_average(matches):
    outs = 0
    notouts = 0
    sum = 0
    for _ in range(matches):
        score, state = [i for i in input().split()][0:2]
        if state == "out":
            sum += int(score)
            outs += 1
        else:
            sum += int(score)
            notouts += 1
    if outs == 0:
        return -1
    else:
        return ceil(sum / outs)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        matches = int(input())
        print(cricket_average(matches))
