"""
Given and integer n. Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists of an integer n. As the output could be large so take mod with 109+7.

Output:
Print the required sum.

Constraints:
1<=T<=100
1<=n<=109

Example:
Input:
2
5
7

Output:
225
784
"""


def sum_of_first_n_terms(n):
    sum = (n * (n + 1) // 2) * (n * (n + 1) // 2)
    return sum % (1000000000 + 7)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_first_n_terms(n))
