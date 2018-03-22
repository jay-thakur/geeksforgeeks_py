"""
A and B are good friend and programmers. They are always in a healthy competition with each other. They decide to judge the best among them by competing. They do so by comparing their three skills as per their values. Please help them doing so as they are busy.

Set for A are like [a1, a2, a3]
Set for B are like [b1, b2, b3]

Compare ith skill of A with ith skill of B
if a[i] > b[i] , A's score increases by 1
if a[i] < b[i] , B's score increases by 1


Input :
The first line of input contains an integer T denoting the Test cases. Then T test cases folllow. The second line of each test case contains Skill values of A . The third line of each test case contains Skill values of B


Output :
For each test case in a new line print the score of A and B separated by space.


Constraints :
1 ≤ T ≤ 50
1 ≤ a[i] ≤ 1017
1 ≤ b[i] ≤ 1017


Example:
Input :
2
4 2 7
5 6 3
4 2 7
5 2 8

Output :
1 2
0 2
"""


def complete_the_skills(set_a, set_b):
    score_a = 0
    score_b = 0
    for i in range(3):
        if int(set_a[i]) > int(set_b[i]):
            score_a += 1
        elif int(set_a[i]) < int(set_b[i]):
            score_b += 1
    return score_a, score_b


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        set_a = [int(i) for i in input().split()][0:3]
        set_b = [int(i) for i in input().split()][0:3]
        score_a, score_b = complete_the_skills(set_a, set_b)
        print(score_a, score_b)