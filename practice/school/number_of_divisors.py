"""
Two friends are playing a game. One gives an integer N  to other and asks: What is the number of divisors of N that are divisible by 3? The task is to help the other friend in finding the number of divisors.

Input:
The first line of input contains an integer T denoting the number of test cases.Then T test cases follow .Each test case consist of an integer N.

Output:
For each test case in a new line print the  number of divisors.

Constraints:

1 ≤ T ≤ 50

1 ≤ N ≤ 100000


Example:

Input:

2

6

10

Output:

2

0

Explanation:

6 has three divisors 1, 3 and 6 out of which two are divisible by 3.
10 has four divisors 1,2,5 and 10 none of which is divisible by 3
"""


def number_of_divisors(n):
    count = 0
    for i in range(3, n + 1):
        if i % 3 == 0 and n % i == 0:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(number_of_divisors(n))