"""
Tywin Lannister is facing a war. He has N troops of soldiers. Each troop has a certain number of soldiers denoted by an array A.
Tywin thinks that a troop is lucky if it has number of soldiers as a multiple of K. He doesn't want to lose any soldiers, so he decides to train some more.
He will win the war if he has atleast half of his troops are lucky troops.
Determine the minimum number of soldiers he must train to win the war.

Input :
First line of input contains a single integer T denoting the number of test cases.
The first line of each test case contains 2 space-separated integers N and K.
The second line contains N space-separated integers A1,A2,A3,...,AN denoting number of soldiers in each troop.

Output :
For each test case, print the required answer in a new line.

Constraints :
1 <= T <= 150
1 <= N <= 100
1 <= K <= 100
1 <= Ai <= 10^4

Example 1 :
Input :
2
5 2
5 6 3 2 1
6 4
2 3 4 9 8 7
Output :
1
1

Explaination :
Case 1 : Troop with 1 soldier is increased to 2.
Case 2 : Troop with 3 soldier is increased to 4.

Example 2 :
Input :
1
4 3
3 1 4 7
Output :
2

Explaination :
Case 1 : Troop with 1 soldier is increased to 3.
"""


def tywins_war_strategy(arr, k):
    arr = [k - m % k for m in arr if (m % k)]
    total = 0
    while len(arr) > n / 2:
        min_a = min(arr)
        arr.remove(min_a)
        total += min_a
    return total


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n]
        print(tywins_war_strategy(arr, k))
