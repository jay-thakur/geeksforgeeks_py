"""
Sambhav is searching for a matching pair. His box is filled with numbers from 1 to N, each number is exactly present twice so there are N pairs. In his worst case scenario, how many numbers 'x' should he pick and remove from his box until he finds a matching pair?

Input:
The first line of input contains an integer T denoting the no of test cases, then T test cases follow. Each test case contains an integer N, which indicates the total pairs of numbers present in the box.


Output:
Print the number of Draws (x) Sambhav makes in the worst case scenario.

Constraints:
1<=T<=500
1<=N<=100000

Example
Input
2
1
2

Output
2
3

Explanation
For first test case
When N=1 Then there is one pair and a matching pair can be extracted in 2 Draws.

For second test case
when N=2 Then there are 2 pairs Let them be {1,2,1,2} and a matching pair will be made in 3 Draws. This can be observed
when we change the permutations of the numbers.
"""


def matching_pair(n):
    return n + 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(matching_pair(n))
