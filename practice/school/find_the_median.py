"""
Given the marks of all students, calculate the median.

Input:
The first line of input takes the number of test cases, T. Then T test cases follow. Each of the T test cases takes 2 input lines.The first line of each test case takes the number of students, N.The second line of each test case takes N space separated integers denoting the marks of all the students.

Output:

Print the floor value of the median for each test case on a new line.

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
61
77
89
"""


def calculate_median(n, arr):
    if n%2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) // 2
    return arr[n//2]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()][0:n]
        print(calculate_median(n, sorted(arr)))