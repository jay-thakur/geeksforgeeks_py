"""
You have a jumpy ball. You throw it up from the ground upto a height of H. The ball is jumpy, so when it comes back to the ground, it rebounds and goes up again to a distance of floor(H/2). This keeps on repeating till it can't rebound anymore. You need to find the total distance travelled by the ball.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains a single line having H as input.

Output:
For each testcase, print the total distance travelled.

Constraints:
1<=T<=105
0<=H<=1015

Example:

Input:
3
10
20
30

Output:
36
76
112

For testcase 1: H is 10. From ground to H it travels d=10. From H to ground it travels d=10+10. Now H becomes
floor(10/2). So ball rebounds to d=10+10+5. It goes down to ground. d=10+10+5+5. Now H becomes floor(5/2). So ball
rebounds to d=10+10+5+5+2. The ball goes down. d=10+10+5+5+2+2. H becomes floor(2/2). So ball rebounds to
d=10+10+5+5+2+2+1. It goes down to ground. d=10+10+5+5+2+2+1+1. H becomes floor(1/2). H is zero so no rebound.
total d=36.
"""


def jumpy_ball(n):
    sum = 0
    while n > 0:
        sum = sum + 2 * n
        n = n // 2
    return sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(jumpy_ball(n))