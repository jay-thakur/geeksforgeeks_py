"""
For two given positive numbers a and b. Find a^b.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, there are two numbers a and b.


Output:
Find a^b.


Constraints:
1 <= T <= 30
1 <= a <= 10
1 <= b <= 10


Example:
Input:
2
1 1
5 2

Output:
1
25
"""


def a_power_b(a, b):
    return a**b


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(a_power_b(a, b))