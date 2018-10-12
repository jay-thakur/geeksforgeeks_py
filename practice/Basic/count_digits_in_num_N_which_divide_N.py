"""
Given a number N, the task is to count all the digits in N which divide N. Divisibility by 0 is not allowed. If any digit in N which is repeated divides N, then all repetitions of that digit should be counted

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the integer N.

Output:

Print the count of all digits of n which divide n for each test case in a new line.

Constraints:
1<= T <=100
1<= No of digits in N <=105

Example:

Input:
2
35
122324

Output:
1
5

Explanation:
For testcase 1: N=35. Now, 3 does not completely divide 35, but 5 does; so our count is 1.

For testcase 2: N=122324. Here, 1 divides N. 2 divides N. Again, 2 divides N. 3 does not divide N.
2 divides N. 4 divides N. So, total number of digits that divide N are 5.
"""


def count_digits_in_num_N_which_divide_N(n):
    counter = 0
    for j in (str(n)):
        if int(j) != 0 and n % int(j) == 0:
            counter += 1
    return counter


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_digits_in_num_N_which_divide_N(n))
