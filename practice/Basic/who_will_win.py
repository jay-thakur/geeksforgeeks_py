"""
Gautam and Subhash are two brothers. They are similar to each other in all respects except one. They have different ways of searching. When Gautam has to search for an item from a lot, he goes through all the items one by one and stops when he finds the item. However Subhash has an entirely different and interesting way of searching. However the search works only for items which are sorted. He goes to the middle of the lot, if he finds the desired item, he stops, if not, he checks whether the middle item is smaller or larger than the required item. If larger, he repeats the same process for the first half of the lot, otherwise second half. One day, the two brothers sit in a contest in which they have to find a name out of a sorted dictionary. Whoever finds out the name first will win the contest. The audience is very eager to know who will win and hence they want you to predict.

Input:

The first line of input takes the number of test cases, T.

The next T lines take the total number of names N, followed by M the position of the name to be searched, as well as the amount of time taken for each observation by Gautam G and Subhash S.

Output:

Print 1 in case Gautam will win, 2 in case Subhash will win, 0 in case of a draw in a separate line.

Constraints:

1<=T<=100

1<=N<=1000

1<=M<=N

1<=G<=100

1<=S<=100

Example:

Input:

3
10 8 10 25
10 8 10 30
10 8 10 12

Output:

2
2
2
"""


def binary_search(n, m, s_t):
    mid = int((n + 1) / 2)
    if mid == m:
        return s_t + s
    elif mid < m:
        return binary_search(n - mid, m - mid, s_t + s)
    else:
        return binary_search(mid - 1, m, s_t + s)


def who_will_win(n, m, g, s):
    g_t = m * g
    s_t = binary_search(n, m, 0)
    if g_t < s_t:
        return 1
    if g_t > s_t:
        return 2
    if g_t == s_t:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m, g, s = [int(i) for i in input().split()][0:4]
        print(who_will_win(n, m, g, s))
