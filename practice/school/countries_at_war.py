"""
The two countries of A and B are at war against each other. Both countries have N number of soldiers. The power of these soldiers are given by A[i]...A[N] and B[i]....B[N].
These soldiers have a pecularity. They can only attack their counterpart enemies, like A[i] can attack only B[i] and not anyone else. A soldier with higher power can kill the enemy soldier. If both soldiers have same power, they both die. You need to find the count of remaining soldiers of A and B at the end of the war. Also, print the winner country.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains three lines of input:-
The number of soldiers N.
Powers of A country's soldiers
Powers of B country's soldiers

Output:
For each testcase, print the remaining soldiers of both A and B, and the winner country. If the remaining soldiers are equal for both countries, the war ends up draw.
See examples for more clarity.

Constraints:
1<=T<=100
1<=N<=2000
0<=A[i]<=1000

Example:

Input:
3
6
1 2 3 4 5 6
6 5 4 3 2 1
1
9
8
2
2 2
5 5

Output:
3 3 DRAW
1 0 A
0 2 B

Explanation:
For testcase3: Both countries have 2 soldiers. B[0] kills A[0], B[1] kills A[1].
A has 0 soldiers alive at the end. B has both soldiers alive at the end. We print the results and B as winner.
"""


def countries_at_war(arr, brr, size):
    count_A = 0
    count_B = 0

    for j in range(size):
        if arr[j] > brr[j]:
            count_A += 1
        if arr[j] < brr[j]:
            count_B += 1

    if count_A > count_B:
        winner = 'A'
    elif count_A < count_B:
        winner = 'B'
    else:
        winner = 'DRAW'

    return count_A, count_B, winner


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [float(i) for i in input().split()][0:size]
        brr = [float(i) for i in input().split()][0:size]
        print(*countries_at_war(arr, brr, size))
