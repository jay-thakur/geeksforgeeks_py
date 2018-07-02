"""
Anand is a great mathematician, he always try new things and want to know the total count of numbers where, N XOR X == N OR X, where 0<=X<=N.

Input:
First line consists of T test cases. Only line of test case consists of integer N.

Output:
Single line output, prints the required output.

Constraints:
1<=T<=10^5
1<=N<=10^18

Example:
Input:
3
5
7
8
Output:
2
1
8

Explanation:
For the first test case
    5 XOR 2 == 5 OR 2
    5 XOR 0 == 5 OR 0
    So the count is 2.
"""


def anands_maths_question(n):
    count = 0
    while n > 0:
        if n & 1 == 0:
            count += 1
        n = n >> 1
    return 2 ** count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(anands_maths_question(n))
