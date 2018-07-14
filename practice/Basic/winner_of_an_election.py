"""
Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidate that received Max votes. If there is tie, print lexicographically smaller name.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains two lines:-
The number of votes cast N
The name of the candidates separated by a space. Each name represents one vote casted to that candidate.

Output:
For each testcase, print the name of the candidate with the maximum votes, and also print the votes casted for the candidate. The name and votes are separated by a space.

Constraints:
1<=T<=105
1<=N<=1000

Example:

Input:
2
13
john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john
3
andy blake clark

Output:
john 4
andy 1

Explanation:
For testcase1: john has 4 votes casted for him, but so does johny. john is lexicographically smaller, so we print john and the votes he received.
For testcase2: We have 3 votes. All the candidates get 1 votes each. We print andy as it is lexicographically smaller.
"""


def winners_of_an_election(arr):
    arr1 = list(set(arr))
    arr1.sort()
    s = []

    for j in range(len(arr1)):
        s.append(arr.count(arr1[j]))
    maxv = max(s)
    return arr1[s.index(maxv)], maxv


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [i for i in input().split()][0:n]
        print(*winners_of_an_election(arr))
