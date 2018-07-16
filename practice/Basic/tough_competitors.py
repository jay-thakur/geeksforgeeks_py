"""
There are N competitors in an exam .Each competitor has his own skill value which is given by the array s=s1,s2,....sN where s1 is the skill of the first competitor,s2 is the skill of second competitor and so on.. Two competitors are said to be tough competitors if their skill difference is least i.e. they are very close in their skill values.Given N and an array s as input,find the tough competitors among the N competitors and print the absolute of the difference of their skill values.

Input:
First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. First line of every test case consists of an integer N, denoting number of competitors. Second line of every test case consists of N spaced separated integers, denoting the skill values of the competitors.

Output:
Corresponding to each test case, print the difference of the skill values of the tough competitors in a new line.

Constraints:
1<=T<=100
2<=N<=100
1<=Si<=10000

Example:
Input:
2
4
9 4 12 6
5
4 9 1 32 12
Output:
2
3

Explanation:

In the first case |9-4|=5 ,|9-12|=3,|9-6|=3,|4-12|=8,|4-6|=2,|12-6|=6 so,the tough competitors are competitors having skill values 4,6 having their skill difference as 2.

In the second case tough competitors are competitors having skill values (4,1) and (9,12)  having their skill difference as 3.
"""


def tough_competitors(arr, size):
    arr.sort()
    m = 100000000000
    for i in range(size - 1):
        if abs(arr[i] - arr[i + 1]) < m:
            m = abs(arr[i] - arr[i + 1])
    return m


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(tough_competitors(arr, size))
