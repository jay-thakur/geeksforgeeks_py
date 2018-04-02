"""
A professor once went to a party. As he did not meet any person of his intellect there, he got bored and started thinking of a problem. The problem was to identify if an ongoing party was an "only boys" party or an “only girls” party. As the rules are strict, no co-ed parties are allowed by the professor's research. After many researches, he came to a conclusion that if all the persons in the party are wearing different colored robes, then that is a girl’s only party. If we even get one duplicate color, it must be a boy’s party. He has now asked you, to code his theorem so that he may move on to more advance research.

Input
The first line of each test case contains an integer T, denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer N denoting the no of people in the party. In the next line are N space separated values of Ai denoting the color of the robes.

Output
For each test case in a new line print “BOYS” without quotes if it’s a boy’s party, else print “GIRLS”.

Constraints
1<=T<=100
1<=N<=100
1<=Ai<=750

Example
Input
2
5
1 2 3 4 7
6
1 3 2 4 5 1

Output
GIRLS
BOYS
"""


def duplicate_found(arr, size):
    s = set()
    c = 0
    for i in range(size):
        if arr[i] in s:
            c = 1
            break
        else:
            s.add(arr[i])
    return c


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print('BOYS' if duplicate_found(arr, size) else 'GIRLS')
