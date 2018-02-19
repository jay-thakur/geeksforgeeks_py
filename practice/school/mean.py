"""
Given the marks of all students, calculate the mean.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case consists of an integer N denoting the number of students. The second line of each test case consists of N space separated integers denoting the marks of all the students.

Output:
Corresponding to each test case, print the floor value of the mean in a new line.

Constraints:
1<=T<=100
1<=N<=100
1<=Marks<=100

Example:

Input:
3
4
56 67 30 79
4
78 89 67 76
5
90 100 78 89 67

Output:
58
77
84
"""


def calculate_mean(n, arr):
    return sum(arr)//n


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()][0:n]
        print(calculate_mean(n, arr))