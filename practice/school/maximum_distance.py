"""
There are n bikes and each can cover 100 km when fully fueled. What is the maximum amount of distance you can go using n bikes? You may assume that all bikes are similar and a bike takes 1 litre to cover 1 km.

The output may contain decimal value but print the integer value of the float value obtained.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print the maximum amount of distance.

Constraints:

1 ≤ T ≤ 20
1 ≤ N ≤ 50

Example:

Input
2
1
2

Output
100

150
"""


def maximum_distance(n_bikes):
    sum = 0.
    for i in range(1, n_bikes+1):
        sum = sum + 100./i
    return int(sum)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n_bikes = int(input())
        print(maximum_distance(n_bikes))