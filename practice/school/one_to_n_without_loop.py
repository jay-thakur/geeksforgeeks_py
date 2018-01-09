"""
Print numbers from 1 to n without the help of loops.

Input:
The first line of the input contains T denoting the number of test cases. First line of test case contain number n.

Output:
Numbers from 1 to n will be printed.

Constraints:

1 <=T<= 100
1 <=N<= 990

Example:

Input:

1
10

Output:

1 2 3 4 5 6 7 8 9 10
"""


def one_to_n_without_loop(num, n):
    if num == n + 1:
        return;

    print(num, end=' ')
    if num != n:
        num += 1
        one_to_n_without_loop(num, n);


if __name__ == '__main__':
    t = int(input())
    num = 1
    for i in range(t):
        n = int(input())
        one_to_n_without_loop(num, n)
        print()